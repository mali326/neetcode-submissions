import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)
        for s in strs:
            ct = [s.count(char) for char in string.ascii_lowercase]
            freqMap[tuple(ct)].append(s)
        return list(freqMap.values())

