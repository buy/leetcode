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
