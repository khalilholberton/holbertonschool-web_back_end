#!/usr/bin/env python3
"""
function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function
    """
    def func(x):
        return x * multiplier
    return func
