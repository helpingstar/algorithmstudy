import sys

n = int(sys.stdin.readline().rstrip())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def check_all_same(x, y, l):
    count = [0, 0]
    for i in range(x, x+l):
        for j in range(y, y+l):
            count[matrix[i][j]] += 1
            if count[0] != 0 and count[1] != 0:
                return False
    if count[0] == 0:
        return [0, 1]
    else:
        return [1, 0]
            

def dy_paper(x, y, l):
    if l == 1:
        count = [0, 0]
        count[matrix[x][y]] += 1
        return count
    is_all_same = check_all_same(x, y, l)
    if is_all_same:
        return is_all_same
    count = [0, 0]
    for i in range(2):
        for j in range(2):
            temp = dy_paper(x + l*i//2, y + l*j//2, l//2)
            count[0] += temp[0]
            count[1] += temp[1]
    return count

result = dy_paper(0, 0, n)
print(*result, sep='\n')