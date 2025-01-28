#!/usr/bin/env python3

'''Task 1: FIFO caching
'''


from typing import Any, Optional
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from
       `BaseCaching` and is a caching system.
    '''

    def __init__(self):
        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        '''put method for adding data to cache
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                cached_data = list(self.cache_data.keys())
                first_key = cached_data[0]

                self.cache_data.pop(first_key)

                print("DISCARD: {}".formart(first_key))

                del first_key
            self.cache_data[key] = item

    def get(self, key: Any) -> Optional[Any]:
        '''get method for reteiving cache
        '''
        return self.cache_data.get(key)

if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "ALX")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
