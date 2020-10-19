#!/usr/bin/env python3
"""
function
"""
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a list
    """
    return [(i, len(i)) for i in lst]
