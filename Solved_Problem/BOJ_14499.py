N, M, x, y, K = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))
    
move_list = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0]

# 정육면체는 가만히 있고 숫자와 판이 움직이는 개념

def roll_dice(move):
    if move == 1:
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    elif move == 2:
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    elif move == 3:
        dice[6], dice[5], dice[1], dice[2] = dice[2], dice[6], dice[5], dice[1]
    elif move == 4:
        dice[6], dice[5], dice[1], dice[2] = dice[5], dice[1], dice[2], dice[6]

for move in move_list:
    # 출력은 주사위 굴림과 x, y좌표의 관계에 대해 독립적이므로 순차적으로 진행해도 된다.
    # 첫번째로 행렬에서의 포인터를 움직이는데 움직이지 못 할경우 continue
    if move == 1:
        if y == M-1:
            continue
        y += 1
    elif move == 2:
        if y == 0:
            continue
        y -= 1
    elif move == 3:
        if x == 0:
            continue
        x -= 1
    elif move == 4:
        if x == N-1:
            continue
        x += 1
    
    roll_dice(move)
    
    # 기타 조건 수행
    if matrix[x][y] == 0:
        matrix[x][y] = dice[6]
    else:
        dice[6] = matrix[x][y]
        matrix[x][y] = 0
    print(dice[1])