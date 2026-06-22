class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        hash= self.hasher(key)
        self.bucket = self.buckets[hash]
        counter=1
        for pair in self.bucket:
            if pair[0] == key:
                pair[1]=value
                counter=0
        if counter!=0:
            self.bucket.append([key,value])

    def get(self, key: int) -> int:
        hash= self.hasher(key)
        self.bucket=self.buckets[hash]
        for pair in self.bucket:
            if pair[0]==key:
                return pair[1]
        else:
            return -1

    def remove(self, key: int) -> None:
        hash= self.hasher(key)
        self.bucket = self.buckets[hash]
        for pair in self.bucket:
            if pair[0] == key:
                self.bucket.remove(pair)

    def hasher(self, key:int ) -> int:
        hash= key%10000
        return hash


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)