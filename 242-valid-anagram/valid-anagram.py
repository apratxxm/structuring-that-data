class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdir={}
        tdir={}
        if len(s) != len(t):
            return False
        for char in s:
                sdir[char]=sdir.get(char, 0)+1
        for char in t:
            tdir[char]=tdir.get(char, 0)+1
            
        for key, value in sdir.items():
            if key not in tdir:
                return False
                return checker
            if sdir[key]!=tdir[key]:
                return False
        return True
