import sys
from collections import deque

input = sys.stdin.readline

wheel_list = []

for _ in range(4):
    wheel = list(input().rstrip())
    wheel_list.append(wheel)

cur = [0, 0, 0, 0]

n = int(input())

def spin(wheel_num, way, visited, direction):
    # print(f'[debug] {wheel_num, way, visited}')
    if not (0 <= wheel_num < 4):
        return
    
    cur[wheel_num] = (cur[wheel_num] - way) % 8
    if direction == 'left':
        if 0 < wheel_num and same[wheel_num-1]:
            spin(wheel_num-1, way*-1, visited, 'left')
    
    if direction == 'right':
        if wheel_num < 3 and same[wheel_num]:
            spin(wheel_num+1, way*-1, visited, 'right')
    
for _ in range(n):
    visited = [False] * 4
    wheel_num, way = map(int, input().split())
    wheel_num -= 1
    
    same = [False] * 3
    for i in range(3):
        left_cur = (cur[i] + 2) % 8
        right_cur = (cur[i+1] - 2) % 8
        # print(f'[debug] {left_cur, right_cur, i}')
        if wheel_list[i][left_cur] != wheel_list[i+1][right_cur]:
            same[i] = True
    
    # print(same)
    
    cur[wheel_num] = (cur[wheel_num] - way) % 8
    
    if 0 < wheel_num and same[wheel_num-1]:
        spin(wheel_num-1, way*-1, visited, 'left')
    if wheel_num < 3 and same[wheel_num]:
        spin(wheel_num+1, way*-1, visited, 'right')
    
    # print(f'[debug] cur: {cur}')

ans = 0

for i in range(4):
    if wheel_list[i][cur[i]] == '1':
        ans += 2 ** i
        
print(ans)