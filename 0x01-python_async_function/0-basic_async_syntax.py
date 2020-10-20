#!/usr/bin/env python3
"""
function
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random
    """
    a = random.uniform(0, max_delay)
    await asyncio.sleep(a)
    return a
