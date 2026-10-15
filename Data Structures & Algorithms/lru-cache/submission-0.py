class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # init LRUCache as a key:value pair dictionary. 
        self.LRUCache = {}

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            temp = self.LRUCache[key]
            del self.LRUCache[key]
            self.LRUCache[key] = temp
            return self.LRUCache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # If LRUCache full. 
        if self.capacity == len(self.LRUCache):
            if key in self.LRUCache:
                del self.LRUCache[key]
            else: 
                del self.LRUCache[list(self.LRUCache.keys())[0]]
            self.LRUCache[key] = value
        else:
            self.LRUCache[key] = value
        

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)