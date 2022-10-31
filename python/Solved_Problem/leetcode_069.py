from typing import *

class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while True:
            if n*n > x:
                return (n-1)
            n += 1
            
            

x = 8
a = Solution()
print(a.mySqrt(x))