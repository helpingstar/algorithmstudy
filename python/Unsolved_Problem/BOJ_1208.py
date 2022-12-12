import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# meet in the middle
arr_1 = arr[:n//2]
arr_2 = arr[n//2:]

subsum_arr_1 = []
subsum_arr_2 = []

for i in range(len(arr_1) + 1):
    # arr_1에서 0 ~ len(arr_1) + 1개만큼 뽑아 만들 수 있는 부분집합의 합을 구한다.
    comb_1 = combinations(arr_1, i)
    for comb in comb_1:
        subsum_arr_1.append(sum(comb))

for i in range(len(arr_2) + 1):
    # arr_2에서 0 ~ len(arr_2) + 1개만큼 뽑아 만들 수 있는 부분집합의 합을 구한다.
    comb_2 = combinations(arr_2, i)
    for comb in comb_2:
        subsum_arr_2.append(sum(comb))

subsum_arr_1.sort()
subsum_arr_2.sort()

left_pointer = 0
right_pointer = len(subsum_arr_2) - 1
ans = 0

while left_pointer < len(subsum_arr_1) and right_pointer >= 0:
    tmp = subsum_arr_1[left_pointer] + subsum_arr_2[right_pointer]

    # 두 포인터가 가르키는 값의 합이 s와 같다면
    if tmp == s:

        # 부분집합의 합이 같은 경우를 예외처리
        same_count_left = 1
        same_count_right = 1

        same_left_idx = left_pointer
        same_right_idx = right_pointer

        left_pointer += 1
        right_pointer -= 1

        while left_pointer < len(subsum_arr_1) and \
                    subsum_arr_1[left_pointer] == subsum_arr_1[same_left_idx]:
            same_count_left += 1
            left_pointer += 1

        while right_pointer >= 0 and \
                    subsum_arr_2[right_pointer] == subsum_arr_2[same_right_idx]:
            same_count_right += 1
            right_pointer -= 1

        ans += same_count_left * same_count_right

    elif tmp < s:
        left_pointer += 1

    else:
        right_pointer -= 1

# 아무것도 뽑지 않는 경우는 고려하지 않으므로, s가 0이라면 해당 경우의 수 1개를 빼준다
if s == 0:
    ans -= 1

print(ans)
