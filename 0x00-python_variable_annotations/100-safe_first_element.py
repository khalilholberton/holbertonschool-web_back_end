#!/usr/bin/env python3
"""
function
"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    safe_first_element
    '''
    if lst:
        return lst[0]
    else:
        return None
