class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter=0
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                temp=nums[k]
                nums[k]=nums[i]
                nums[i]=temp
                k+=1
        for num in nums:
            if num!=val:
                counter+=1
            else: break
        return counter

