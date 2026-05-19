class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ''.join(char.lower() for char in s if char.isalnum())
        return True if cleanS == cleanS[::-1] else False