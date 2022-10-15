class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = p_ptr = 0
        while p_ptr < len(p):
            now = p[p_ptr]
            if now == '.':
