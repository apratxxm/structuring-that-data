class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tptr=0
        sptr=0
        while (tptr<len(t) and sptr<len(s)):
            pts=s[sptr]
            ptt=t[tptr]

            if ptt == pts:
                tptr+=1
                sptr+=1
            elif ptt!=pts :
                tptr+=1

        if sptr == len(s):
            return True
        else:
            return False
             


            

            

            