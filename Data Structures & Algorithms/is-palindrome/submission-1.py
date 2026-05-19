class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(filter(str.isalnum, s.lower()))
        return True if s2 == s2[::-1] else False