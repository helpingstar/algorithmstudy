import sys

input = sys.stdin.readline

n, m = map(int ,input().split())

memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int ,input().split()))

tc = sum(costs)

arr = [[0 for _ in range(tc+1)] for _ in range(n+1)]
result = sys.maxsize

for i in range(1, n+1):
    memory = memories[i]
    cost = costs[i]
    for j in range(1, tc+1):
        if j < cost:
            arr[i][j] = arr[i-1][j]
        # 이 문제의 경우 m을 넘는 것중 최소라는 조건이 있기 때문에 (.. < m) 이라는
        # 조건이 있어도 풀렸지만 최대의 값을 구할 경우 없애는 것이 맞다
        # elif ... -> else
        elif j >= cost and arr[i-1][j] < m:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-cost] + memory)
        if arr[i][j] >= m:
            result = min(j, result)

print(result)