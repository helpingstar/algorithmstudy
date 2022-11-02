from typing import *

class Solution:
    def __init__(self):
        self.ans = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.dp(nums, [], len(nums))
        return self.ans
    def dp(self, src, maked, count):
        if count == 0:
            self.ans.append(maked)
            return
        for i in range(count):
            # print(f'[debug]  {src}, {maked}')
            self.dp(src[:i]+src[i+1:], maked + [src[i]], count - 1)
            
a = Solution()
nums = [0, 1]
print(a.permute(nums))