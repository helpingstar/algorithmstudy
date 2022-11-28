class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        minus = True
        if (dividend < 0) == (divisor < 0):
            minus = False
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        for i in range(32, -1, -1):
            if dividend >= (divisor * (1 << i)):
                dividend -= (divisor * (1 << i))
                result += (1 << i)
        if minus:
            return -min(2 << 31, result)
        else:
            return min(result, (2 << 30)-1)
