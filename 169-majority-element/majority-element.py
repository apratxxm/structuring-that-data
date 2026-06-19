class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        n=len(nums)
        for element in nums:
            map[element]=map.get(element,0)+1
            if map[element]>n/2:
                return element
        