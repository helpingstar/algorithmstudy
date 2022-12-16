from collections import defaultdict
from typing import *
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
            if dic[num] > len(nums) // 2:
                return num
