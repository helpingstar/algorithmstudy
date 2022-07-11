import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append([max(a, b), min(a, b)])
    
    arr.sort()
    
    dp = [0] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i][0] >= arr[j][0] and arr[i][1] >= arr[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) + 1

print(solution())
