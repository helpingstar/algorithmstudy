from collections import deque
from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        q = deque()
        q.append((0, len(nums)-1))
        while q:
            left, right = q.popleft()
            # print(left, right)
            if left == right:
                continue
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                if mid - left == 1:
                    return nums[mid]
                q.append((left, mid))
            if nums[mid] > nums[right]:
                if right - mid == 1:
                    return nums[right]
            # else:
                q.append((mid, right))
        return nums[0]
