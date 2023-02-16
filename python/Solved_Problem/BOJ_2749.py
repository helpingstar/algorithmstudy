import sys
import copy
input = sys.stdin.readline

n = int(input())

def mul(a, b, size):
    temp = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                temp[i][j] += a[i][k] * b[k][j]
            temp[i][j] %= 1000000
    return temp

identity = [[1, 0], [0, 1]]
multiplier = [[0, 1], [1, 1]]

cursor = copy.deepcopy(multiplier)

cnt = 1

if n & 1 == 1:
    result = copy.deepcopy(multiplier)
else:
    result = copy.deepcopy(identity)

while (1 << cnt) <= n:
    cursor = mul(cursor, cursor, 2)
    if n & (1 << cnt) != 0:
        result = mul(result, cursor, 2)
    cnt += 1
        

print(result[0][1])