class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted_array = self.shorter(nums)
        return sorted_array

    def shorter(self, nums: List[int])->List[int]:
        length=len(nums)
        if length>1:
            mid = length//2
            left  =nums[:mid]
            right =nums[mid:]
            if len(left)>1:
                left = self.shorter(left)
            if len(right)>1:
                right = self.shorter(right)
            common=[]
            if left[-1]<=right[0]:
                common=left+right
                return common
            else:
                i=0
                j=0
                while i <len(left) and j <len(right):
                    if left[i]>right[j]:
                        common.append(right[j])
                        j+=1
                    elif right[j]>=left[i]:
                        common.append(left[i])
                        i+=1
                common.extend(left[i:])
                common.extend(right[j:])
                return common
        else: return(nums)


        