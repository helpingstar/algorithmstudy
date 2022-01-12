import sys

n = int(sys.stdin.readline().rstrip())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip())))

def check_all_same(x, y, l):
    num_table_for_check_same = [0, 0]
    for i in range(x, x+l):
        for j in range(y, y+l):
            num_table_for_check_same[matrix[i][j]] += 1
            if num_table_for_check_same[0] != 0 and num_table_for_check_same[1] != 0:
                return False
    if num_table_for_check_same[0] != 0:
        return [1, 0]
    else:
        return [0, 1]

def dy_qt(x, y, l):
    if l == 1:
        return '({})'.format(matrix[x][y])
    if l == 2:
        if matrix[x][y] + matrix[x][y+1] + matrix[x+1][y] + matrix[x+1][y+1] == 0:
            return '0'
        elif matrix[x][y] + matrix[x][y+1] + matrix[x+1][y] + matrix[x+1][y+1] == 4:
            return '1'
        else:
            return '({}{}{}{})'.format(matrix[x][y], matrix[x][y+1], matrix[x+1][y], matrix[x+1][y+1])
    
    check_same = check_all_same(x, y, l)
    if check_same:
        if check_same[0] == 1:
            return '0'
        else:
            return '1'
    else:
        return '(' + dy_qt(x, y, l // 2) + dy_qt(x, y + l//2, l//2) + dy_qt(x + l//2, y, l // 2) + dy_qt(x+ l//2, y+ l//2, l // 2) + ')'

print(dy_qt(0, 0, n))