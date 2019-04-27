import collections
from cache import Cache
import random
class RandomCache(Cache):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def get(self, key):
        for (k,v) in self.cache:
            if k==key:
                return v
        return None

    def set(self, key, value):
        while(len(self.cache) >= self.capacity):
            self.cache.pop(random.randint(0,len(self.cache)-1))
        self.cache.append((key,value))