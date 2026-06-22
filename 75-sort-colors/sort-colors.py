class Solution:
    def sortColors(self, nums: List[int]) -> None:
        map={}
        for num in nums:
            map[num]=map.get(num,0)+1
        red_count = map.get(0,0)
        white_count = map.get(1,0)
        blue_count = map.get(2,0)
        nums[:]= [0] * red_count + [1]*white_count + [2]*blue_count