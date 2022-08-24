import sys

input = sys.stdin.readline

n_weight = int(input())
weights = list(map(int, input().split()))
n_target = int(input())
targets = list(map(int, input().split()))

board = [[0 for _ in range(i*500 + 1)] for i in range(n_weight+1)]

def dp(num, weight):
    if num > n_weight:
        return
    if board[num][weight]:
        return
    
    board[num][weight] = 1

    dp(num+1, weight)
    dp(num+1, weight+weights[num-1])
    dp(num+1, abs(weight-weights[num-1]))

dp(0, 0)

ans = []

for t in targets:
    if t > sum(weights):
        ans.append('N')
        continue
    if board[n_weight][t]:
        ans.append('Y')
    else:
        ans.append('N')

print(*ans)
