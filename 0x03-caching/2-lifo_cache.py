#!/usr/bin/python3
"""
cashing system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache inherits from BasicCashing
    """

    def __init__(self):
        """
        init method
        """
        super().__init__()
        self.disip = []

    def get(self, key):
        """
        return the value of key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None

    def put(self, key, item):
        """
        this is the function put
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.disip[-1]]
                    print("DISCARD:", self.disip[-1])
                    self.disip.pop(-1)
                self.cache_data[key] = item
            self.disip.append(key)
