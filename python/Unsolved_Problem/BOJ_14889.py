import sys
from itertools import combinations

def solution():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    combis = list(combinations(range(n), n//2))
    ans = sys.maxsize
    for comb in combis[:len(combis)//2]:
        print(comb)
        s_abil = 0
        l_abil = 0
        for i in range(n):
            for j in range(n):
                if i in comb and j in comb:
                    s_abil += board[i][j]
                    s_abil += board[j][i]
                elif i not in comb and j not in comb:
                    l_abil += board[i][j]
                    l_abil += board[j][i]
        ans = min(ans, abs(s_abil - l_abil))

    return ans


print(solution())
