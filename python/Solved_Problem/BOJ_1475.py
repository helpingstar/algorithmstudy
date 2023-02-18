import sys
import math
input = sys.stdin.readline

num = input().rstrip()

num_list = [0] * 9

for n in num:
    n = int(n)
    
    if n in {6, 9}:
        num_list[6] += 1
    else:
        num_list[n] += 1
# print(num_list)
ans = 0
for i in range(9):
    if i == 6:
        ans = max(ans, math.ceil(num_list[6] / 2))
    else:
        ans = max(ans, num_list[i])
print(ans)