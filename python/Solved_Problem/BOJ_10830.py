import sys

input = sys.stdin.readline

size, target = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(size)]

def dot(m1, m2):
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += m1[i][k] * m2[k][j]
            result[i][j] %= 1000
    return result

answer = [[0] * size for _ in range(size)]
for i in range(size):
    answer[i][i] = 1

while target != 0:
    if target % 2 == 1:
        answer = dot(answer, mat)
    target //= 2
    mat = dot(mat, mat)

for i in answer:
    print(*i)
