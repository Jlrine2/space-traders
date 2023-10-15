from requests.exceptions import HTTPError


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
            return [model(**x) for x in data]
        return model(**resp.json()["data"])
