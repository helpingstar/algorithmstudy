class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        L = len(nums)
        for i in range(L-2):
            left, right = i+1, L-1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    if [nums[i], nums[left], nums[right]] not in ans:
                        ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return ans
