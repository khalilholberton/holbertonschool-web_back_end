#!/usr/bin/env python3
"""
This module contains teh class Cache
"""


import redis
from functools import wraps
from typing import Union, Callable, Optional
import uuid


def count_calls(method: Callable) -> Callable:
    """
    count how many times methods of the Cache class are called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        wrapper method
        """
        method_key = method.__qualname__
        self._redis.incr(method_key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call_history method
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        wrapper
        """
        method_key = method.__qualname__
        meth_inputs = method_key + ':inputs'
        meth_outputs = method_key + ":outputs"
        data = str(args)
        self._redis.rpush(meth_inputs, data)
        res = method(self, *args, **kwds)
        self._redis.rpush(meth_outputs, str(res))
        return res
    return wrapper


def replay(method: Callable):
    """
    replay
    """
    rd = redis.Redis()
    method_key = method.__qualname__
    meth_inputs = "".join([key, ":inputs"])
    meth_outputs = "".join([key, ":outputs"])
    ctr = method.__self__.redis
    ctr = ctr.get(method_key).decode("utf-8")
    print(f"{method_key} was called {ctr} times:")
    inp_list = redis.lrange(meth_inputs, 0, -1)
    outp_list = redis.lrange(meth_outputs, 0, -1)
    d = list(zip(inp_list, outp_list))
    for x, y in d:
        attr, res = x.decode("utf-8"), y.decode("utf-8")
        print("{}(*{}) -> {}".format(method_key, attr), res)


class Cache():
    """
    class Cache
    """
    def __init__(self):
        """
        __init__() method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store() method
        """
        randomKEY = str(uuid.uuid4())
        self._redis.set(randomKEY, data)
        return randomKEY

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        get() method
        """
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    def get_str(self, key):
        """
        get_str() method
        """
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key):
        val = self._redis.get(key)
        return int(val)
