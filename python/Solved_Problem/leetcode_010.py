class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # print(f'[debug] "{s}", "{p}"')
        if not p:
            return not s

        first_match = False
        if s and p[0] in {s[0], '.'}:
            first_match = True
        
        if len(p) >= 2 and p[1] == '*':
            if first_match:
                if self.isMatch(s[1:], p):
                    return True
            
            if self.isMatch(s, p[2:]):
                return True
        else:
            if first_match:
                if self.isMatch(s[1:], p[1:]):
                    return True
        return False

a = Solution()
s = "abb"
p = "ab*"

print(a.isMatch(s, p))