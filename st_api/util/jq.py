import json

import pyjq


def _dictify(model):
    return json.loads(model.model_dump_json())


def jq(query, data):
    model_type = type(data[0])
    res = pyjq.all(f".[] | select({query})", [_dictify(m) for m in data])
    return [model_type(**m) for m in res]
