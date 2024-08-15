class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'}': '{', ')': '(', ']': '['}
        stack = []
        if len(s) % 2 != 0:
            return False

        for char in s:

            if char in valid:
                stack.pop()
                
                if stack[-1] != valid[char] and stack:
                    return False
                
                
            else:
                stack.append(char)
        
        return not stack
        