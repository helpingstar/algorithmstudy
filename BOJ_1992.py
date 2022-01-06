import sys

n = int(sys.stdin.readline().rstrip())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def dy_qt(x, y, l):
    if l == 1:
        return '({})'.format(matrix[x][y])
    if l == 2:
        return '({}{}{}{})'.format(matrix[x][y], matrix[x][y+1], matrix[x+1][y], matrix[x+1][y+1])
    
    return '(' + dy_qt(x, y, l // 2) + dy_qt() + dy_qt() + dy_qt() + ')'