import functools
from collections import Counter



def cache(f, maxsize=100):
    @functools.wraps(f)
    def deco(*args):
        if args in deco._cache:
            counter = Counter()
            for key, value in deco_cache.items():
                counter[key] = 0
                for v in value:
                    if v in value:
                        counter[key] += 1
                        to_delete = min(counter.values())
                        if len(deco._cache) >= maxsize:
                            deco._cache.pop(to_delete)
            return deco._cache[args]
        result = f(*args)
        deco._cache[args] = result
        return result
    deco._cache = {}
    return deco





