nums = [2,2,2,2,2]
target = 8

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)-3):
            target_1 = target - nums[i]
            for j in range(i+1, len(nums)-2):
                if j > (i+1) and nums[i] == nums[i-1]:
                    continue

                target_2 = target_1 - nums[j]
                
                left = j+1
                right = len(nums)-1
                
                while left < right:
                    if nums[left] + nums[right] == target_2:
                        # sorted를 쓰려고 했으나 i, j, left, right는 정렬상태임
                        if [nums[i], nums[j], nums[left], nums[right]] not in answer:
                            answer.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -=1
                        left += 1
                        right -=1
                    elif nums[left] + nums[right] < target_2:
                            left += 1
                    else:
                            right -= 1
        return answer

a = Solution()
print(a.fourSum(nums, target))