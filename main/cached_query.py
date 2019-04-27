from uncached_query import UncachedQuery
from lru_cache import LRUCache
from fifo_cache import FIFOCache
from random_cache import RandomCache
class CachedQuery(UncachedQuery):
    
    def setup_cache(self,typ,capacity):
        if(typ=='lru'):
            self.cache = LRUCache(capacity)
        if(typ=='fifo'):
            self.cache = FIFOCache(capacity)
        if(typ=='random'):
            self.cache = RandomCache(capacity)
            
    def exec_query_with_cache(self,query_string):
        val = self.cache.get(query_string)
        if val != None:
            return val
        else:
            val = self.exec_query(query_string)
            self.cache.set(query_string,val)
            return val