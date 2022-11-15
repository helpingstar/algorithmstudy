import sys

input = sys.stdin.readline

n_house, n_router = map(int, input().split())

house_position_list = [int(input()) for _ in range(n_house)]
house_position_list.sort()

left, right = 0, house_position_list[-1] - house_position_list[0]
ans = -1

while left <= right:
    mid = left + (right-left) // 2
    # print(f'[debug]  mid : {mid}')
    prev = 0
    answer = 0
    num = 1
    for i, pos in enumerate(house_position_list[1:], 1):
        if pos - house_position_list[prev] >= mid:
            prev = i
            num += 1
    # print(f'[debug]  num : {num}')
    if num >= n_router:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
