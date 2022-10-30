class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        for i in range(m+n-2, m+n-2-(n-1), -1):
            ans *= i
        for i in range(2, n):
            ans //= i
        return ans
