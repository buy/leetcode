
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

import collections

# 3:15

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.queue = collections.deque()
        self.capacity = capacity
        self.cache = {}

    # @return an integer
    def get(self, key):
        self.cache.get(key, -1)
        print key
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return
        
        self.cache[key] = value
        if len(self.queue) == self.capacity:
            del self.cache[self.queue.popleft()]
        self.queue.append(key)

s = LRUCache(1)
s.set(2,1)
s.get(2)
s.set(3,2)
s.get(2)
s.get(3)
