class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N, i = len(nums), 0
        while i < N:
            while 1<=nums[i]<=N:
                idx_expected = nums[i]-1
                if nums[i] == nums[idx_expected]:
                    break
                nums[i], nums[idx_expected] = nums[idx_expected], nums[i]
            i = i + 1
        for i in range(N):
            if nums[i] != i+1:
                return i+1
        return N+1
