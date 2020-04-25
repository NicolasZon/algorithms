"""
LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.
"""
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    # O(1)
    def get(self, key: int) -> int:
        ans = self.cache.get(key)
        if ans is not None:
            self.cache.move_to_end(key)
            return ans
        return -1

    # O(1)
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(False)


x = []
cache = LRUCache(2)
x.append(cache.put(2, 1))
x.append(cache.put(1, 1))
x.append(cache.put(2, 3))
x.append(cache.put(4, 1))
x.append(cache.get(1))
x.append(cache.get(2))
print(x)

x = []
cache = LRUCache(2)
x.append(cache.put(1, 1))
x.append(cache.put(2, 2))
x.append(cache.get(1))
x.append(cache.put(3, 3))
x.append(cache.get(2))
x.append(cache.put(4, 4))
x.append(cache.get(1))
x.append(cache.get(3))
x.append(cache.get(4))
print(x)
