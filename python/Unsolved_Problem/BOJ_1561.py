import sys

input = sys.stdin.readline

n_child, n_play = map(int, input().split())
t_list = list(map(int, input().split()))

if n_child < n_play:
    print(n_child)
else:
    # 이분 탐색
    left, right = 0, 60000000000
    while left <= right:
        mid = (left + right) // 2
        cnt = n_play
        for i in range(n_play):
            cnt += mid // t_list[i]
        if cnt >= n_child:  # n명을 태울 수 있는 상황
            t = mid
            right = mid - 1
        else:
            left = mid + 1
    # t : n_child를 모두 태우는 시간

    # t - 1에 탑승한 아이들의 숫자를 계산한다.
    cnt = n_play
    for i in range(n_play):
        cnt += (t - 1) // t_list[i]

    # t에 탑승한 아이를 계산한다.
    for i in range(n_play):
        if t % t_list[i] == 0:  # t 시간에 탑승한 아이
            cnt += 1
        if cnt == n_child:
            print(i + 1)
            break
