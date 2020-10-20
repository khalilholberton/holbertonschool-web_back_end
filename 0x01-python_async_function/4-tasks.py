#!/usr/bin/env python3
"""
coroutine
"""

from typing import List
import asyncio
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    def
    task_wait_n
    """
    tyme = [
        wait_random(max_delay) for i in range(n)
    ]
    tot = []
    for element in asyncio.as_completed(tyme):
        col = await element
        tot.append(col)
    return tot
