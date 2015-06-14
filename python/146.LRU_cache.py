
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

import collections

# 3:15

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.freshness = collections.deque([])
        self.capacity = capacity
        self.cache = {}

    # @return an integer
    def get(self, key):
        if key in self.cache:
            self.freshness.remove(key)
            self.freshness.append(key)

        return self.cache.get(key, -1)

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                del self.cache[self.freshness.popleft()]
        else:
            self.freshness.remove(key)

        self.freshness.append(key)
        self.cache[key] = value

s = LRUCache(1)
s.set(2,1)
s.get(2)
s.set(3,2)
s.get(2)
s.get(3)
print s.cache
