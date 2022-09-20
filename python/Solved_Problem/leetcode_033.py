class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left = 0
        # right = len(nums) - 1
        # answer = -1
        length = len(nums)
        left, right = 0, length - 1

        if length == 0:
            return -1

        while left <= right:
            # mid = (left + right) // 2
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # mid < right
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
