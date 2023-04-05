import sys
import math

input = sys.stdin.readline

n_min, n_max = map(int, input().split())

is_square = [True] * (n_max - n_min + 1)

ans = n_max - n_min + 1

for i in range(2, math.ceil((n_max)**0.5) + 1):
    square = i * i

    for j in range(square * math.ceil(n_min / square), n_max+1, square):
        if is_square[j-n_min]:
            ans -= 1
            is_square[j-n_min] = False

print(ans)
