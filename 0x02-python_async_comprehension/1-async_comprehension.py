#!/usr/bin/env python3
"""                                                                                      
async                                                                                    
"""
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """                                                                                  
    async                                                                                
    """
    oper = [a async for a in async_generator()]
    return oper
