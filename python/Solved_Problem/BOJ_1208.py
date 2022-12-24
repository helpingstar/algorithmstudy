import sys
from itertools import combinations

input = sys.stdin.readline

n, target = map(int, input().split())

num_list = list(map(int, input().split()))

num_list_1 = num_list[:n//2]
num_list_2 = num_list[n//2:]

left = []
right = []

for i in range(len(num_list_1) + 1):
    for comb in combinations(num_list_1, i):
        left.append(sum(comb))

for i in range(len(num_list_2) + 1):
    for comb in combinations(num_list_2, i):
        right.append(sum(comb))
        
left.sort()
right.sort()

l_cur = 0
r_cur = len(right) - 1

result = 0

while l_cur < len(left) and r_cur >= 0:
    tmp = left[l_cur] + right[r_cur]
    if tmp == target:
        tmp_l_cur, tmp_r_cur = l_cur, r_cur
        l_cur += 1
        r_cur -= 1
        while l_cur < len(left) and left[tmp_l_cur] == left[l_cur]:
            l_cur += 1
        
        while  r_cur >= 0 and right[tmp_r_cur] == right[r_cur]:
            r_cur -= 1
        
        result += (l_cur - tmp_l_cur) * (tmp_r_cur - r_cur)
    elif tmp > target:
        r_cur -= 1
    else:
        l_cur += 1

if target == 0:
    result -= 1
print(result)
        