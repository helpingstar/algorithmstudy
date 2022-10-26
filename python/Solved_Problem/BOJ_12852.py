import sys

input = sys.stdin.readline

n = int(input())

arr = [[-1, []] for _ in range(n+1)]

for i in range(1, n+1):
    arr[i][0] = arr[i-1][0] + 1
    arr[i][1] = arr[i-1][1] + [i]

    if i % 3 == 0 and arr[i][0] > arr[i//3][0] + 1:
        arr[i][0] = arr[i//3][0] + 1
        arr[i][1] = arr[i//3][1] + [i]

    if i % 2 == 0 and arr[i][0] > arr[i//2][0] + 1:
        arr[i][0] = arr[i//2][0] + 1
        arr[i][1] = arr[i//2][1] + [i]


print(arr[n][0])
print(*reversed(arr[n][1]))
