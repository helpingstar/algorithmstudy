import sys
import bisect

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))
num_ord = sorted(set(num_list))

result = []
for i in num_list:
    result.append(bisect.bisect_left(num_ord, i))

print(*result)