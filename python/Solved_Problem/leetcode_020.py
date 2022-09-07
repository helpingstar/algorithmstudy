from collections import deque

match = {'(':')', '{':'}', '[':']'}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False
                elif match[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False
        else:
            return True