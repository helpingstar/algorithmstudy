from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(list(map(str, digits))))
        number += 1
        return list(map(int, str(number)))


digits = [1, 2, 3, 4, 5]
a = Solution()
print(a.plusOne(digits))
