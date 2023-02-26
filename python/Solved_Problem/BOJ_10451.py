import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    
    temp = list(map(int, input().split()))
    map_num = {i+1 : temp[i] for i in range(n)}
    
    visited = [False] * (n+1)
    result = 0
    
    for i in range(1, n+1):
        if not visited[i]:
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cur = map_num[cur]
            result += 1
    return result
            
T = int(input())

for _ in range(T):
    print(solution())