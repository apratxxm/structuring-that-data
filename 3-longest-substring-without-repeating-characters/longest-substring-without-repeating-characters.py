class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        freq={}
        maxi=0
        left=0

        for right in range(len(s)):
            char=s[right]
            freq[char]=freq.get(char,0)+1

            while freq[char]>1:
                freq[s[left]]-=1
                left+=1
            
            length=right-left+1
            maxi=max(maxi,length)
        return maxi

        

