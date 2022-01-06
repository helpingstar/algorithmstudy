# 변수를 최대한 줄여야 한다.
# 공통된 성격의 변수는 합치자
# x1, x2, y1, y2로 할 것이 아니라 x1, y1, l 로 합치자

import sys

n = int(sys.stdin.readline().rstrip())

matrix = []

for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    matrix.append(line)

def is_all_same(x1, x2, y1, y2):
    count_box = [0] * 3
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            count_box[matrix[i][j] + 1] += 1
            if not ((count_box[0] == 0 and count_box[1] == 0) or (count_box[0] == 0 and count_box[2] == 0) or (count_box[1] == 0 and count_box[2] == 0)):
                return False
    all_square = (x2 - x1 + 1) * (x2 - x1 + 1)
    if count_box[0] == all_square:
        return [1, 0, 0]
    elif count_box[1] == all_square:
        return [0, 1, 0]
    else:
        return [0, 0, 1]

def dy_matrix(x1, x2, y1, y2):
    if x2 - x1 == 2:
        # 9개짜리의 각 숫자의 개수를 저장하기 위함
        count_33 = [0, 0, 0]
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                count_33[matrix[i][j] + 1] += 1
        if count_33[0] == 9:
            return [1, 0, 0]
        elif count_33[1] == 9:
            return [0, 1, 0]
        elif count_33[2] == 9:
            return [0, 0, 1]
        else:
            return count_33
        
    check_is_all_same = is_all_same(x1, x2, y1, y2)
    if check_is_all_same:
        return check_is_all_same
    else:
        # 9개 구역의 누적합을 구하기 위함
        count_num = [0, 0, 0]
        # 한 변의 길이
        unit = (x2 - x1 + 1) // 3
        for i in range(3):
            for j in range(3):
                temp = dy_matrix(x1 + unit*i, x1 + unit*(i+1) - 1, y1 + unit*j, y1 + unit*(j+1) - 1)
                count_num[0] += temp[0]
                count_num[1] += temp[1]
                count_num[2] += temp[2]
    return count_num

if n == 1:
    result = [0, 0, 0]
    result[matrix[0][0] + 1] = 1
else:
    result = dy_matrix(0, n-1, 0, n-1)

for i in result:
    print(i)