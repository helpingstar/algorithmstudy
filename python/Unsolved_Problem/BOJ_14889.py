import sys
from itertools import combinations


def solution():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    combis = list(combinations(range(n), n//2))
    ans = sys.maxsize
    for comb in combis:
        # print(comb)
        s_abil = 0
        l_abil = 0
        not_comb = []
        for i in range(n):
            if i not in comb:
                not_comb.append(i)

        for i in comb:
            for j in comb:
                s_abil += board[i][j]
                s_abil += board[j][i]
        for i in not_comb:
            for j in not_comb:
                l_abil += board[i][j]
                l_abil += board[j][i]
        ans = min(ans, abs(s_abil - l_abil))

    return ans


print(solution())
