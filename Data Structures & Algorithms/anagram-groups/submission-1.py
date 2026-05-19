class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charDict = {}
        for s in strs:
            x = ''.join(sorted(s))
            if x not in charDict:
                charDict[x] = [s]
            else:
                charDict[x].append(s)
        return list(charDict.values())