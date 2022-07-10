def query(cmd, value, file):
    if "filter" == cmd:
        res = list(filter(lambda x: value in x, file))
        return res
    if "map" == cmd:
        res = list(map(lambda x: x.split()[int(value)], file))
        return res
    if "unique" == cmd:
        res = list(set(file))
        return res
    if "sort" == cmd:
        reverse = value == 'desc'
        res = list(sorted(file, reverse=reverse))
        return res
    if "limit" == cmd:
        val = int(value)
        res = list(file)[:val]
        return res

