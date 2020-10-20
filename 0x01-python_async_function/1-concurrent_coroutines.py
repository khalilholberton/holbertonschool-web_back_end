#!/usr/bin/env python3
"""
coroutine
"""
import random
from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    func
    wait_n
    """
    a = await asyncio.gather(*(wait_random(max_delay) for ctr in range(n)))
    return sorted(a)
