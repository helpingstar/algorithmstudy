from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0
        stack = [float('inf')]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                ans += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            ans += stack.pop() * stack[-1]
        return ans
