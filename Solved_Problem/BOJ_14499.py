N, M, x, y, K = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))
    
move_list = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0]

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
    
    if matrix[x][y] == 0:
        matrix[x][y] = dice[6]
    else:
        dice[6] = matrix[x][y]
        matrix[x][y] = 0
    print(dice[1])