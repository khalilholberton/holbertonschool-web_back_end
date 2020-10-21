#!/usr/bin/env python3
"""
async
"""
import random
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine
    """
    x = time.time()
    col = [async_comprehension() for a in range(4)]
    await asyncio.gather(*col)
    res = time.time() - x
    return res
