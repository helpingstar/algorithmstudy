from typing import *
# from itertools import combinations

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         length = len(nums)
#         for i in range(length+1):
#             for comb in combinations(nums, i):
#                 result.append(list(comb))

#         return result

# -------------------------------------------------------------

class Solution:
    def __init__(self):
        self.result = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        for i in range(length+1):
            self.dp([], nums, i)
        return self.result

    def dp(self, arr, rest_arr, target):
        if len(arr) == target:
            self.result.append(arr)
            return
        if len(rest_arr) < target-len(arr):
            return
        for i in range(len(rest_arr)):
            self.dp(arr + [rest_arr[i]], rest_arr[i+1:], target)

nums = [1,2,3]
a = Solution()
print(a.subsets(nums))
