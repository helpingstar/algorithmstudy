def check(haystack, needle, h_cur):
    if len(needle) > len(haystack) - h_cur:
        return False

    for i in range(len(needle)):
        if haystack[h_cur + i] != needle[i]:
            return False
    return True

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if check(haystack, needle, i):
                return i
        return -1
