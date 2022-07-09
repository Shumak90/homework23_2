from flask import abort


def query(cmd, value, file):
    if "filter" == cmd:
        res = list(filter(lambda x: value in x, file))
        return res
    if "map" == cmd:
        try:
            res = list(map(lambda x: x.split()[int(value)], file))
            return res
        except Exception:
            return abort(400, 'value is not int')
    if "unique" == cmd:
        res = list(set(file))
        return res
    if "sort" == cmd:
        reverse = value == 'desc'
        res = list(sorted(file, reverse=reverse))
        return res
    if "limit" == cmd:
        try:
            res = list(file[:int(value)])
            return res
        except Exception:
            return abort(400, 'value is not int')


