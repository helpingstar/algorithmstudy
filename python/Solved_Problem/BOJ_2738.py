row, col = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(row)]

for i in range(row):
    temp = list(map(int, input().split()))
    for j in range(col):
        a[i][j] += temp[j]

for i in range(row):
    print(*a[i])
