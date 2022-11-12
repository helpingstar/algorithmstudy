class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for idx in range(len(s) + 1):
            one = two = 0

            if idx >= 2 and 10 <= int(s[idx-2:idx]) <= 26:
                two = 1
            if idx >= 1 and 1 <= int(s[idx-1]) <= 9:
                one = 1

            if one:
                dp[idx] += dp[idx-1]
            if two:
                dp[idx] += dp[idx-2]
        return dp[len(s)]

s = "12"
a = Solution()
print(a.numDecodings(s))
