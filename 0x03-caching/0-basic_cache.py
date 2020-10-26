#!/usr/bin/python3
"""
This module contains class BasicCache
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    this is the class BasicCache
    """
    def put(self, key, item):
        '''
        this is function put
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''
        this is function get
        '''
        if key in self.cache_data:
            return self.cache_data[key]
        return None
