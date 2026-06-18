class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdir={}
        tdir={}
        checker=True
        if len(s) != len(t):
            return False
        for char in s:
                sdir[char]=sdir.get(char, 0)+1
        for char in t:
            tdir[char]=tdir.get(char, 0)+1
            
        for key, value in sdir.items():
            try:
                if not sdir[key]==tdir[key]:
                    checker=False
                    return checker
            except KeyError:
                checker=False
                return checker
        return checker
