class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        maxLen = 0
        for ch in s:
            if ch not in substr:
                substr += ch
            else:
                i = substr.index(ch)
                substr = substr[i+1:]
                substr += ch
            maxLen = max(maxLen, len(substr))
        return maxLen