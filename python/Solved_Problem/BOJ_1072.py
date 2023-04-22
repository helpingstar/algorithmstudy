import sys
import math
input = sys.stdin.readline

x, y = map(int, input().split())

p = (100 * y // x) + 1


if y * 100 // x >= 99:
    print(-1)
else:
    print(math.ceil((p*x - 100*y)/(100-p)))
