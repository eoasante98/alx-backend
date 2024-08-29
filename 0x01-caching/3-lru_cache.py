#!/usr/bin/python3
'''
A class LRUCache that inherits from BaseCaching and is a caching system
'''


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''
    A Class that inherits BaseCaching and upon attempt to add an
    entry to the cache when it is at max capacity, it discards the least
    recently used entry to accomodate for the new one
    Attributes:
        __init__ - method that initializes class instance
        put - method that adds a key/value pair to cache
        get - method that retrieves a key/vale pair from cache
    '''

    def __init__(self):
        '''Initialize class instance'''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        '''Adds key/value pair to cache data'''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        '''Return value stored in key of value in cache'''
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
