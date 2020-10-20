#!/usr/bin/env python3
"""
coroutine
"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time
    """
    beg = time.time()
    asyncio.run(wait_n(n, max_delay))
    tim = (time.time() - beg)
    return (tim / n)
