import json
import sonic
import strings
from flask import Response

json_content_type = ["application/json; charset=utf-8"]
jsonp_content_type = ["application/javascript; charset=utf-8"]
json_ascii_content_type = ["application/json"]

def json_response(ret_code_pointer, ret_json_pointer):
    body, err = sonic.MarshalString(ret_json_pointer)
    if err != None:
        return Response("RetData-Marshal-Error:" + str(err), status=500, content_type="text/plain")

    response = Response(body, status=ret_code_pointer, content_type="application/json")
    return response

def secure_json_response(ret_code_pointer, ret_json_pointer):
    body, err = sonic.MarshalString(ret_json_pointer)
    if err != None:
        return Response("RetData-Marshal-Error:" + str(err), status=500, content_type="text/plain")

    if strings.HasPrefix(body, "[") and strings.HasSuffix(body, "]"):
        body = app_conf.secure_json_prefix + body

    response = Response(body, status=ret_code_pointer, content_type="application/json")
    return response
