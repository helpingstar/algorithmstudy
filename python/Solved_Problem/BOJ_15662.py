import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(deque(map(int, list(input().rstrip()))))

n_turn = int(input())

def turn(q:deque, way):
    if way == 1:
        temp = q.pop()
        q.appendleft(temp)
    if way == -1:
        temp = q.popleft()
        q.append(temp)

def turn_top(num, way):

    ns = [False] * n
    for i in range(n-1):
        if arr[i][2] != arr[i+1][6]:
            ns[i] = True
    
    # check left
    l_ptr = num-2
    l_way = 1 if way==-1 else -1
    while l_ptr >= 0 and ns[l_ptr]:
        turn(arr[l_ptr], l_way)
        l_ptr -= 1
        l_way = 1 if l_way==-1 else -1
    
    # check right
    r_ptr = num-1
    r_way = 1 if way==-1 else -1
    while r_ptr < n and ns[r_ptr]:
        turn(arr[r_ptr+1], r_way)
        r_ptr += 1
        r_way = 1 if r_way==-1 else -1
    
    turn(arr[num-1], way)

for _ in range(n_turn):
    num, way = map(int, input().split())
    turn_top(num, way)
    
cnt = 0
for deq in arr:
    if deq[0] == 1:
        cnt += 1
        
print(cnt)