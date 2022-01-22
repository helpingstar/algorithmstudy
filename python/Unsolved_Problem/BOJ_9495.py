import sys
input = sys.stdin.readline

t = int(input())

def get_highest_score(matrix, n):
    if n == 1:
        return max(matrix[0][0], matrix[1][0])
    if n == 2:
        return max(matrix[0][0] + matrix[1][1], matrix[1][0] + matrix[0][1])
    score = []
    for _ in range(2):
        score.append([0] * n)
    score[0][0], score[1][0] = matrix[0][0], matrix[1][0]
    score[0][1], score[1][1] = matrix[0][1] + matrix[1][0], matrix[0][0] + matrix[1][1]
    for i in range(2, n):
        score[0][i] = max(score[1][i-2], score[1][i-1]) + matrix[0][i]
        score[1][i] = max(score[0][i-2], score[1][i-1]) + matrix[1][i]
    return max(score[0][n-1], score[1][n-1])

for _ in range(t):
    matrix = []
    n = int(input())
    for _ in range(2):
        matrix.append(list(map(int, input().split())))
    print(get_highest_score(matrix, n))