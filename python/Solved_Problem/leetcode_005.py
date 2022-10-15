class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        
        if s == 1:
            return s
        ans = s[0]
        longest_num = 1
        for i in range(length-1):
            l, r = i, i+1
            while  0 <= l  and r < length and s[l] == s[r]:
                if r - l + 1 > longest_num:
                    ans = s[l:r+1]
                    longest_num = r - l + 1
                l -= 1
                r += 1
            l ,r = i, i
            while 0 <= l and r < length and s[l] == s[r]:
                if r - l + 1 > longest_num:
                    ans = s[l:r+1]
                    longest_num = r - l + 1
                l -= 1
                r += 1
        return ans