nums = [-1,2,1,-4]
target = 1

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        len_nums = len(nums)
        answer = 100000
        for i in range(len_nums-2):
            l = i+1
            r = len_nums - 1

            target_diff = target - nums[i]
            while l < r:
                if nums[l] + nums[r] == target_diff:
                    return target
                elif nums[l] + nums[r] < target_diff:
                    if abs(answer-target) > abs(target_diff - nums[l] - nums[r]):
                        answer = nums[i] + nums[l] + nums[r]
                    l += 1
                else:
                    if abs(answer-target) > abs(target_diff - nums[l] - nums[r]):
                        answer = nums[i] + nums[l] + nums[r]
                    r -= 1
        return answer

a = Solution()
print(a.threeSumClosest(nums, target))