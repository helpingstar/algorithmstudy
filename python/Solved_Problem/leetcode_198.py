class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, nums[0]]
        for n in nums[1:]:
            dp = [max(dp), dp[0] + n]
        
        return max(dp)