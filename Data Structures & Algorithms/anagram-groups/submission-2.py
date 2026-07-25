from collections import defaultdict
class Solution:
    # make dict with key as sorted word, value as list of words made of those char
    # return list of values

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = defaultdict(list)
        for s in strs:
            temp = ''.join(sorted(s)) #sort s
            chars[temp].append(s)
        return list(chars.values())

    