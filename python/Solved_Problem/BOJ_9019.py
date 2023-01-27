import sys
from collections import deque

input = sys.stdin.readline
INF = 20000
T = int(input())

def func_D(num):
    return (2*num) % 10000

def func_S(num):
    if num == 0:
        return 9999
    else:
        return num-1

def func_L(num):
    temp = num // 1000
    return (num * 10 + temp) % 10000

def func_R(num):
    temp = num % 10
    return (num // 10 + temp * 1000)

def solution():
    visited = [False] * 10000
    start, target = map(int, input().split())
    visited[start] = True
    q = deque()
    q.append((start, ''))
    while q:
        now, trace = q.popleft()
        # print(now)
        for name, func in [('D', func_D), ('S', func_S), ('L', func_L), ('R', func_R)]:
            next_num = func(now)
            if next_num == target:
                return trace + name
            # print(check[next_num][0], check[now][0])
            if visited[next_num]:
                continue
            q.append((next_num, trace+name))
            visited[next_num] = True


for _ in range(T):
    print(solution())
