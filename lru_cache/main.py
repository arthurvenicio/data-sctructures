class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        if capacity <= 0:
            raise TypeError("You must pass a positive number to capacity")
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        # print(self.cache)
        if key not in self.cache:
            return -1
        
        self.cache[key] = self.cache.pop(key)
        return self.cache[key]
          

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
           self.cache.pop(key)
        
        self.cache[key] = value
        
        # print(self.cache)
        
        if len(self.cache) > self.capacity:
           self.cache.pop(next(iter(self.cache)))
        
            
lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
print(lRUCache.get(1));    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2));    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1));    # return -1 (not found)
print(lRUCache.get(3));    # return 3
print(lRUCache.get(4));    # return 4


# here we use dictonary (hashmap)  