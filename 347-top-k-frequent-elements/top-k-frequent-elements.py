class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for num in nums:
            map[num]=map.get(num,0)+1
        common=[]
        max=0
        sorted_keys = sorted(map.keys(), key=lambda x: map[x] )
        return sorted_keys[-k:]


       