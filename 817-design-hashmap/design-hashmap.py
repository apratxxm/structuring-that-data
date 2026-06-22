class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        hash= self.hasher(key)
        self.bucket = self.buckets[hash]
        if key not in self.bucket:
            self.bucket.append(key)
            self.bucket.append(value)
        else:
            idx=self.bucket.index(key)
            self.bucket[idx]=key
            self.bucket[idx+1]=value

    def get(self, key: int) -> int:
        hash= self.hasher(key)
        self.bucket=self.buckets[hash]
        if key in self.bucket:
            idx=self.bucket.index(key)
            return self.bucket[idx+1]
        else:
            return -1

    def remove(self, key: int) -> None:
        hash= self.hasher(key)
        self.bucket = self.buckets[hash]
        if key in self.bucket:
            idx=self.bucket.index(key)
            valueidx=idx+2
            self.bucket[idx:valueidx]=[]

    def hasher(self, key:int ) -> int:
        hash= key%10000
        return hash


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)