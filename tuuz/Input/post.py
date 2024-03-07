from flask import request, abort


class Input:
    @staticmethod
    def post(key, need_xss=False):
        in_data = request.form.get(key)
        if not in_data:
            abort(400, f"POST-[{key}]")
        else:
            if need_xss:
                # TODO: 需要完成xss过滤这里
                out = (in_data)
                return out, True
            else:
                return in_data, True

    @staticmethod
    def post_null(key, need_xss=False):
        in_data = request.form.get(key)
        if not in_data:
            return "", True
        else:
            if need_xss:
                out = xss.filter_xss(in_data)
                return out, True
            else:
                return in_data, True
