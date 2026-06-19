class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        starting= strs[0]
        for entry in strs:
            while entry.find(starting)!=0:
                starting=starting[0:-1]
        if not starting:
            return ""
        else:
            return starting
