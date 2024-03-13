def key_params(**kwargs):
    result = {}
    for k, v in kwargs.items():
        if isinstance(v, (list, dict)):
            v = str(v)
        result[v] = k
    return result


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)