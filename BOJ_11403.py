import sys

n = int(sys.stdin.readline().rstrip())
matrix = []
x_one = set()
y_one = set()
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    matrix.append(line)
    for j in range(n):
        if line[j] == 1:
            x_one.add(i)
            y_one.add(j)
x_one = list(x_one)
y_one = list(y_one)

for i in x_one:
    for j in y_one:
        matrix[i][j] = 1
        
for line in matrix:
    print(*line)