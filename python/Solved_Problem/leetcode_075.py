class Solution:
    def sortColors(self, nums: List[int]) -> None:
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
