from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                new_target = target - nums[i] - nums[j]
                l, r = j+1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < new_target:
                        l += 1
                    elif nums[l] + nums[r] > new_target:
                        r -= 1
                    else:
                        if [nums[i], nums[j], nums[l], nums[r]] not in answer:
                            answer.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
        return answer

a = Solution()
print(a.fourSum([1,0,-1,0,-2,2], 0))
