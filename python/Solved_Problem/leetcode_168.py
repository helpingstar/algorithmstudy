alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def exsh(num):
            if num < 26:
                return alphabet[num]
            return exsh(num // 26 - 1) + alphabet[num % 26]

        return exsh(columnNumber-1)
