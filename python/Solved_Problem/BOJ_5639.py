import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)

arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break

def dp(arr):
    if len(arr) < 2:
        return arr
    cur = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[0]:
            cur = i
            break

    if cur:
        return dp(arr[1:cur]) + dp(arr[cur:]) + [arr[0]]
    else:
        return dp(arr[1:]) + [arr[0]]

print(*dp(arr), sep='\n')
