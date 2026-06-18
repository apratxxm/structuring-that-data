class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for s in strs:
            letters=[]
            for letter in s:
                letters.append(letter)
            letters="".join(sorted(letters))
            if letters not in map :
                map[letters]=[]
            map[letters].append(s)
        results=[]
        for value in map.values():
            results.append(value)
        return results

        