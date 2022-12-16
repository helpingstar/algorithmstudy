class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, alphabet in enumerate(columnTitle):
            result *= 26
            result += (ord(alphabet) - ord('A') + 1)
        return result
