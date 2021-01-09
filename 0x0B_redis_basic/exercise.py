#!/usr/bin/env python3
"""
This module contains teh class Cache
"""


import redis
from typing import Union, Callable, Optional
import uuid


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
