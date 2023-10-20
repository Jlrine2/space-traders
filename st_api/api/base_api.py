import json
from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from requests.exceptions import HTTPError
import pyjq


class SpaceTradersError(BaseException):
    pass


def _handle_http_error(resp):
    try:
        resp.raise_for_status()
    except HTTPError as e:
        error = resp.json()["error"]
        raise SpaceTradersError(
            f"Space traders error: {error['code']}\n {error['message']}\n{error['data']}"
        )
    
    
def _dictify(model):
    return json.loads(model.model_dump_json())


class Collection(list):
    def __init__(self, iterable, model_type):
        self.model_type = model_type
        super().__init__(iterable)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(list))

    def select(self, q):
        res = pyjq.all(f".[] | select({q})", [_dictify(m) for m in self])
        return Collection((self.model_type(**m) for m in res), self.model_type)


class BaseApi:
    def __init__(self, session, base_url, meta_callback) -> None:
        self.session = session
        self.base_url = base_url
        self.meta_callback = meta_callback

    def _get(self, url, query_params=None):
        if query_params is None:
            query_params = {}
        resp = self.session.get(f"{self.base_url}/{url}", params=query_params)
        resp.raise_for_status()
        return resp

    def _post(self, url, body=None):
        if body is None:
            body = {}
        resp = self.session.post(f"{self.base_url}/{url}", json=body)
        resp.raise_for_status()
        return resp

    def _patch(self, url, body=None):
        if body is None:
            body = {}
        resp = self.session.patch(f"{self.base_url}/{url}", json=body)
        resp.raise_for_status()
        return resp

    def _parse(self, resp, model, nesting=None):
        j = resp.json()
        data = j["data"]
        if "meta" in j:
            self.meta_callback(j["meta"])
        if nesting:
            for n in nesting:
                j = j[nesting]
        if isinstance(data, list):
            return Collection((model(**x) for x in data), model)
        return model(**resp.json()["data"])
