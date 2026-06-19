class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        n=len(nums)
        for element in nums:
            map[element]=map.get(element,0)+1
        for key, value in map.items():
            if value > n/2:
                return key
        