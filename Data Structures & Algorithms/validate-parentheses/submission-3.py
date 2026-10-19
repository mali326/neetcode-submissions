class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0: #if everything doesnt have a pair, false
            return False
            
        stack = []
        for i in range(len(s)):
            if s[i] == "[" or s[i] == '(' or s[i] == '{':
                stack.append(s[i])
            else: #if s[i] == "]" or s[i] == ')' or s[i] == '}':
                if len(stack) == 0:
                    return False
                opening = stack.pop()
                if (s[i] == "]" and opening != "[") or (s[i] == ")" and opening != "(") or (s[i] == "}" and opening != "{"):
                    return False

        return True if len(stack)==0 else False