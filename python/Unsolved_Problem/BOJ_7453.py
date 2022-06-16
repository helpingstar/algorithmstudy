"""
Branch and Bound로 풀려다가 실패하였다.

import sys
import bisect
input = sys.stdin.readline

n = int(input())
board = [[], [], [], []]
for _ in range(n):
    abcd = list(map(int, input().split()))
    for i in range(4):
        board[i].append(abcd[i])

for i in range(4):
    board[i].sort()

max_bound = []
min_bound = []

for i in range(1, 4):
    max_n = 0
    min_n = 0
    for j in range(i, 4):
        max_n += board[j][-1]
        min_n += board[j][0]
    max_bound.append(max_n)
    min_bound.append(min_n)
zero_cnt = 0

def dp(cnt, num):
    global zero_cnt
    if cnt == 3:
        if num + (board[3][bisect.bisect_left(board[3], -num)]) == 0:
            zero_cnt += bisect.bisect_right(board[3], -num) - bisect.bisect_left(board[3], -num)
    else:
        for board_num in board[cnt]:
            next_num = board_num + num
            if -max_bound[cnt] <= next_num <= -min_bound[cnt]:
                dp(cnt + 1, next_num)

dp(0, 0)

print(zero_cnt)
"""

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    # arr.shape: (n, 4)
    arr = [list(map(int, input().split())) for _ in range(n)]
    ab, cd = [], []
    for i in range(n):
        for j in range(n):
            # ab, cd를 더한 경우의 수를 모두 append한다.
            ab.append(arr[i][0] + arr[j][1])
            cd.append(arr[i][2] + arr[j][3])

    # 투 포인터를 하기 위하여 ab, cd를 정렬한다.
    ab.sort()
    cd.sort()
    i, j = 0, len(cd) - 1 # i는 ab의 시작점, j는 cd의 끝점(투포인터)
    result = 0
    while i < len(ab) and j >= 0:
        if ab[i] + cd[j] == 0: # 합이 0이 되는 경우
            nexti, nextj = i + 1, j - 1
            # ab가 같은게 여러개인경우 : nexti를 계속 오른쪽으로 이동시킨다
            while nexti < len(ab) and ab[i] == ab[nexti]: 
                nexti += 1
            # cd가 같은게 여러개인경우 : nextj를 계속 왼쪽으로 이동시킨다.
            while nextj >= 0 and cd[j] == cd[nextj]: 
                nextj -= 1

            # i의 이동횟수 X j의 이동횟수
            result += (nexti - i) * (j - nextj) 
            i, j = nexti, nextj
        # ab + cd가 0보다 큰 경우 cd를 왼쪽으로 이동해야 줄일 수 있다.
        elif ab[i] + cd[j] > 0: 
            j -= 1
        else: 
            i += 1

    print(result)