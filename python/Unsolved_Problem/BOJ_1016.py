import sys
import math

input = sys.stdin.readline

is_square_num = set()

a, b = map(int, input().split())

for i in range(2, math.ceil(math.sqrt(b))):
    square = i * i
    cnt = 1
    while cnt * square <= b:
        is_square_num.add(cnt*square)
        cnt += 1
answer = 0
for i in range(a, b+1):
    if i not in is_square_num:
        answer += 1

print(answer)
