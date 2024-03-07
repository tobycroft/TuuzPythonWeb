import json
from typing import Any, Dict, Tuple

import config.app
import config.secure
import tuuz.Ret.response


def json_encode(data: Any) -> str:
    return json.dumps(data)


def success(code: int, data: Any = None, echo: Any = None) -> None:
    if echo is None:
        echo_map = {
            0: "成功",
            -1: "登录失效请重新登录",
            400: "参数错误",
            401: "鉴权失败",
            403: "权限不足",
            404: "未找到数据",
            406: "数据不符合期待",
            407: "数据不符合期待",
            500: "数据库错误"
        }
        echo = echo_map.get(code, "失败")

    if isinstance(echo, Exception):
        echo = str(echo)

    if data is None:
        data = []

    ret_code, ret_json = ret_succ(code, data, echo)
    if config.secure.SECURE_JSON:
        return tuuz.Ret.response.secure_json_response(ret_json)
    else:
        return tuuz.Ret.response.json_response(ret_json)


def fail(code: int, data: Any = None, echo: Any = None) -> None:
    return success(code, data, echo)


def ret_succ(code: int, data: Any = None, echo: Any = None) -> Tuple[int, Dict[str, Any]]:
    ret_code = 200 if code == 0 else 200
    if data is None:
        data = []
    return ret_code, {"code": code, "data": data, "echo": echo}


def ret_fail(code: int, data: Any, echo: Any) -> Tuple[int, Dict[str, Any]]:
    return ret_succ(code, data, echo)


def ws_succ(typ: str, code: Any, data: Any, echo: Any) -> str:
    ret = {"type": typ, "code": code, "data": data, "echo": echo}
    try:
        return json_encode(ret)
    except Exception as e:
        print(e)
        return ""


def ws_succ2(typ: str, route: str, code: Any, data: Any, echo: Any) -> str:
    ret = {"type": typ, "route": route, "code": code, "data": data, "echo": echo}
    try:
        return json_encode(ret)
    except Exception as e:
        print(e)
        return ""


def ws_fail(typ: str, code: Any, data: Any, echo: Any) -> str:
    return ws_succ(typ, code, data, echo)
