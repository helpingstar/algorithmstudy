import sys
from itertools import combinations
input = sys.stdin.readline


def solution():
    target = int(input())
    n_A = int(input())
    a_list = list(map(int, input().split()))
    n_B = int(input())
    b_list = list(map(int, input().split()))
    a_sum = [0]
    b_sum = [0]

    for i in range(n_A):
        a_sum.append(a_sum[-1] + a_list[i])

    for i in range(n_B):
        b_sum.append(b_sum[-1] + b_list[i])
    a_sub = []
    for i in range(n_A):
        for j in range(i+1, n_A+1):
            a_sub.append(a_sum[j] - a_sum[i])

    b_sub = []
    for i in range(n_B):
        for j in range(i+1, n_B+1):
            b_sub.append(b_sum[j] - b_sum[i])

    a_sub.sort()
    b_sub.sort()

    a_cur = 0
    b_cur = len(b_sub)-1

    ans = 0

    while a_cur < len(a_sub) and b_cur >= 0:
        temp = a_sub[a_cur] + b_sub[b_cur]
        if temp < target:
            a_cur += 1
        elif temp > target:
            b_cur -= 1
        else:
            a_cnt = 1
            b_cnt = 1
            while a_cur < len(a_sub) - 1 and a_sub[a_cur] == a_sub[a_cur+1]:
                a_cnt += 1
                a_cur += 1
            while b_cur > 0 and b_sub[b_cur] == b_sub[b_cur-1]:
                b_cnt += 1
                b_cur -= 1
            a_cur += 1
            b_cur -= 1
            ans += (a_cnt * b_cnt)
    print(ans)


solution()
