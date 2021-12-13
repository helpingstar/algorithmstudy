import sys

n = int(sys.stdin.readline())
dict = {0:0}
max_num = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    if num in dict.keys():
        dict[num] += 1
    else:
        dict[num] = 1
    if dict[num] > dict[max_num]:
        max_num = num
    elif dict[num] == dict[max_num]:
        if num < max_num:
            max_num = num

print(max_num)