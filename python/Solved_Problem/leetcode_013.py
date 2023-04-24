class Solution:
    def romanToInt(self, s: str) -> int:
        a2n = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        temp = a2n[s[0]]
        for i in range(1, len(s)):
            if a2n[s[i-1]] < a2n[s[i]]:
                result += a2n[s[i]] - temp
                temp = 0
            elif a2n[s[i-1]] == a2n[s[i]]:
                temp += a2n[s[i]]
            else:
                result += temp
                temp = a2n[s[i]]
        result += temp

        return result
