import sys

input = sys.stdin.readline

N, L = map(int, input().split())

board = [[0] * L for _ in range(4)]
dmap = {'A': 0, 'C': 1, 'G': 2, 'T':3}
dmap2 = 'ACGT'
for i in range(N):
    word = input().rstrip()

    for j in range(L):
        board[dmap[word[j]]][j] += 1

ans = ''
answer = 0
for i in range(L):
    temp = 0
    ans_temp = ''
    sum_temp = 0
    for j in range(4):
        sum_temp += board[j][i]
        if temp < board[j][i]:
            ans_temp = dmap2[j]
            temp = board[j][i]
    ans += ans_temp
    answer += (sum_temp - temp)

print(ans)
print(answer)
