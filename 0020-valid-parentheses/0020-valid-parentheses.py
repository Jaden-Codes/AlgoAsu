class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'}': '{', ')': '(', ']': '['}
        stack = []
        if len(s) % 2 != 0:
            return False

        for char in s:

            if char in valid:
                
                
                if stack[] == valid[char] and stack:
                    stack.pop()
                else:
                    return False
                
                
            else:
                stack.append(char)
        
        return not stack
        