from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        l = 0
        charlist = defaultdict(int)
        ans = 0
        temp = 0
        for r in range(length):
            charlist[s[r]] += 1
            temp += 1
            if charlist[s[r]] == 2:
                while charlist[s[r]] != 1:
                    charlist[s[l]] -= 1
                    l += 1
                    temp -= 1
            ans = max(ans, temp)
        return ans