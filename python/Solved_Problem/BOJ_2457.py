"""
4
3 1 4 1
4 1 5 1
5 1 6 1
7 1 12 1
ans : 0

# 다음 코드를 그냥 적음 -> 의미없음
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cum_days = [0] * 12
for i in range(11):
    cum_days[i+1] = cum_days[i] + days[i]
    
시간복잡도 : O(n)
"""

import sys

cum_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]


def day_to_int(month, day):
    global cum_days
    return cum_days[month-1] + day


def solution():
    input = sys.stdin.readline

    start, end = day_to_int(3, 1), day_to_int(11, 30)
    N = int(input())

    flowers = []
    for _ in range(N):
        m1, d1, m2, d2 = map(int, input().split())
        flowers.append((day_to_int(m1, d1), day_to_int(m2, d2)))

    flowers.sort()
    # line : 취할수 있는 꽃의 상한선
    line = start
    max_line = 0
    cnt = 0

    for l, r in flowers:
        if l <= line:
            if r > end:
                return cnt + 1
            max_line = max(max_line, r)
        else:
            if l <= max_line:
                cnt += 1
                if r > end:
                    return cnt + 1
                line = max_line
                max_line = r
            else:  # 새로운 시작일이 기존 max_line에 못미칠 경우 빈 공간이 생긴다
                return 0
    return 0


if __name__ == "__main__":
    print(solution())
