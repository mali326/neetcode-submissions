import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = re.sub('[^a-zA-Z0-9]','',s)
        return True if s1.lower() == s1[::-1].lower() else False