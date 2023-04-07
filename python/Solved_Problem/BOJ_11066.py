import sys

input = sys.stdin.readline
INF = sys.maxsize
for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    sums = [0] * (N+1)
    for i in range(N):
        sums[i+1] = nums[i] + sums[i]

    dp = [[0] * N for _ in range(N)]
    # print(f'sums: {sums}')
    for size in range(1, N):
        for start in range(N-size):
            temp = INF
            end = start + size
            for mid in range(start, end):
                temp = min(temp, dp[start][mid] + dp[mid+1][end])
            dp[start][end] = temp + sums[end+1] - sums[start]
    # for i in dp:
    #     print(i)
    print(dp[0][N-1])
