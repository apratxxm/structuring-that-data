class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        #Forward Pass: Calculate prefix products
        left_multiplier = 1
        for i in range(n):
            # Place the current product of everything to the left into answer[i]
            answer[i] = left_multiplier
            # Update the multiplier to include the current number for the next index
            left_multiplier *= nums[i]
            
        #Backward Pass: Calculate suffix products and combine
        right_multiplier = 1
        # Loop backwards from n-1 down to 0
        for i in range(n - 1, -1, -1):
            # Multiply the existing left product by the product of everything to the right
            answer[i] *= right_multiplier
            # Update the multiplier to include the current number for the next index
            right_multiplier *= nums[i]
            
        return answer