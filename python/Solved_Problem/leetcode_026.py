class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer = 1
        cur = 0
        back_cur = 1
        while back_cur < len(nums):
            if nums[cur] < nums[back_cur]:
                nums[cur+1], nums[back_cur] = nums[back_cur], nums[cur+1]
                cur += 1
                answer += 1
                
            back_cur += 1
            
        return answer