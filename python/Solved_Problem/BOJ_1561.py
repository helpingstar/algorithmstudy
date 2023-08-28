import sys

def solution():
    input = sys.stdin.readline

    n_child, n_play = map(int, input().split())
    times = list(map(int, input().split()))

    if n_child <= n_play:
        return n_child

    result = None

    left, right = 0, 60000000000
    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for t in times:
            cnt += (mid // t) + 1

        if n_child <= cnt:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    temp = 0

    for t in times:
        temp += ((result - 1) // t) + 1

    for i, t in enumerate(times, 1):
        if result % t == 0:
            temp += 1
            if temp == n_child:
                return i

print(solution())
