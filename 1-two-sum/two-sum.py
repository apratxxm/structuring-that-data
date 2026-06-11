class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}

        for i,num in enumerate(nums):
            blech=target-num
            if blech in hash:
                return[hash[blech],i]
            else:
                hash[num]=i


            