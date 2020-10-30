#!/usr/bin/env python3
"""
This modeule cintains index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range"""
    a = page * page_size - page_size
    b = a + page_size
    return (a, b)
