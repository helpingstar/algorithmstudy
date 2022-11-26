from collections import defaultdict
from typing import *

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        n_max = max(nums)
        dp = defaultdict(int)
        parent = dict()
        ans = 1

        def find_parent(parent, x):
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])
            return parent[x]

        def union_parent(parent, a, b):
            nonlocal ans
            a = find_parent(parent, a)
            b = find_parent(parent, b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b
            dp[a] = dp[b] = dp[a] + dp[b]
            ans = max(ans, dp[a])
        for num in nums:
            if num not in parent:
                parent[num] = num
            if dp[num]:
                continue
            dp[num] = 1
            if dp[num+1]:
                union_parent(parent, num, num+1)
            if dp[num-1]:
                union_parent(parent, num, num-1)
        return ans
