from datetime import datetime
from functools import wraps
from time import time


def log_run(fun):
    def func(*args, **kwargs):
        start = time()
        print(f"{datetime.now().isoformat()}| function {fun.__name__} called with:")
        print(f"{len(args)} positional arguments")
        print(f"optional parameters: {', '.join(list(kwargs.keys())) if len(kwargs.keys()) > 0 else '-'}")
        out = fun(*args, **kwargs)
        print(f"returned: {out} ({(time() - start):.2e})")
    return func

@log_run
def fun(*args, **kwargs):
    pass


if __name__ == '__main__':
    decorated_sum = log_run(sum)
    decorated_sum([1,2,3])
    fun(1, 2, 'a', bb=1)
    # Przykładowy log
    # 2020-01-23T21:09:55| function sum called with:
    # 1 postional parameters
    # optional parameters: -
    # returned: 6 (1.43e-06s)
    # 2020-01-23T21:09:55| function fun called with:
    # 3 postional parameters
    # optional parameters: bb
    # returned: None (1.43e-06s)
