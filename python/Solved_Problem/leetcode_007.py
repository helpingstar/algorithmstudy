class Solution:
    def reverse(self, x: int) -> int:
        is_minus = x < 0
        
        x = int(str(abs(x))[::-1])
        
        if is_minus:
            if -x < -(2 << 30):
                return 0
        else:
            if x > ((2 << 30) - 1):
                return 0
            
        if is_minus:
            return -x
        else:
            return x
        
a = Solution()
print(a.reverse(1463847412))