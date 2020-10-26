#!/usr/bin/python3
"""
caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BasicCaching
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
            self.disip.remove(key)
            self.disip.append(key)
            return self.cache_data[key]
        return None

    def put(self, key, item):
        """
        this is the class put
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.disip.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.disip[0]]
                    print("DISCARD:", self.disip[0])
                    self.disip.pop(0)
                self.cache_data[key] = item
            self.disip.append(key)
