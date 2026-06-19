class MyHashSet:

    def __init__(self):
        self.buckets= [ [] for _ in range(10000) ]



    def add(self, key: int) -> None:
        hash=self.hasher(key)
        bucket=self.buckets[hash]
        if key not in bucket:
            bucket.append(key)


        

    def remove(self, key: int) -> None:
        hash=self.hasher(key)
        bucket=self.buckets[hash]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        hash=self.hasher(key)
        bucket=self.buckets[hash]
        return key in bucket

    def hasher(self, key: int)->int:
        hash=key%10000
        return hash

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)