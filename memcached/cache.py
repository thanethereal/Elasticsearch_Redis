import functools
import time
from random import *


def timestamped_lru_cache(maxsize=None):
    cache = {}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func, args, frozenset(kwargs.items()))
            current_time = time.time()

            if key in cache:
                result, timestamp = cache[key]
                print(f"Cache hit! Result retrieved from cache (timestamp: {timestamp})")
                return result

            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            print(f"Cache miss! Result calculated and stored in cache (timestamp: {current_time})")
            return result

        def get_cached_result(*args, **kwargs):
            key = (func, args, frozenset(kwargs.items()))
            if key in cache:
                result, timestamp = cache[key]
                return result
            else:
                return None

        wrapper.get_cached_result = get_cached_result
        return wrapper

    return decorator

@timestamped_lru_cache(maxsize=None)
def calculate_sum(x, y):
    return x + y

calculate_sum(8, 3)

calculate_sum(2, 3)

calculate_sum(6, 3)

calculate_sum(2, 3)

# Get previously calculated result from cache
previous_result = calculate_sum.get_cached_result(2, 3)
print("Previous result from cache:", previous_result)