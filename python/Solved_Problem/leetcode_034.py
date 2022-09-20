import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if nums == []:
            return [-1, -1]

        b_left = bisect.bisect_left(nums, target)
        b_right = bisect.bisect_right(nums, target)

        if b_left == len(nums):
            return [-1, -1]

        if nums[b_left] == target and nums[b_left] == nums[b_right-1]:
            return [b_left, b_right-1]
        else:
            return [-1, -1]
