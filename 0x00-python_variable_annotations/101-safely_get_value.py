#!/usr/bin/env python3
"""
function
"""
from typing import Union, Any, Tuple, Mapping, TypeVar


tVar = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any, default: Union[tVar, None]=None
                     ) -> Union[Any, tVar]:
    '''
    safely_get_value
    '''
    if key in dct:
        return dct[key]
    else:
        return default
