class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(min(strs, key=len))
        answer = ''
        for i in range(length):
            for word in strs[1:]:
                if word[i] != strs[0][i]:
                    return answer
            answer += strs[0][i]
        return answer
