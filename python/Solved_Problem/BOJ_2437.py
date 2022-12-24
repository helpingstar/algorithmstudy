import sys

input = sys.stdin.readline

n = int(input())

weight_list = list(map(int, input().split()))

weight_list.sort()

target = 1

for weight in weight_list:
    if weight <= target:
        target += weight
    else:
        break

print(target)