class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for element in nums:
            map[element]=map.get(element, 0)+1
            if map[element]>1:
                return True
        return False

        