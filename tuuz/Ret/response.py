import json

from flask import Response

import config.secure

json_content_type = ["application/json; charset=utf-8"]
jsonp_content_type = ["application/javascript; charset=utf-8"]
json_ascii_content_type = ["application/json"]


def json_response(data):
    body = json.dumps(data, indent=4, sort_keys=True, default=str)
    response = Response(body, content_type="application/json")
    return response


def secure_json_response(data):
    body = json.dumps(data)
    if isinstance(data, list) and len(data) > 0:
        body = config.secure.SECURE_JSON_PREFIX + body

    response = Response(body, content_type="application/json")
    return response
