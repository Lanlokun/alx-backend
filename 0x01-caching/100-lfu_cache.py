#!/usr/bin/python3
""" LFU Caching """


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []
        self.lfu = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discard = self.queue.pop(0)
                    del self.cache_data[discard]
                    del self.lfu[discard]
                    print("DISCARD: {}".format(discard))
            elif key in self.cache_data:
                self.queue.remove(key)
                self.lfu[key] += 1
            else:
                self.lfu[key] = 0
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            self.lfu[key] += 1
            return self.cache_data[key]
        return None
