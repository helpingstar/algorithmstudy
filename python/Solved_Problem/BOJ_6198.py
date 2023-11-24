import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n_building = int(input())
    ans = 0
    mem = deque()
    for _ in range(n_building):
        height = int(input())
        if not mem:
            mem.append(height)
        else:
            while mem and mem[-1] <= height:
                mem.pop()
            ans += len(mem)
            mem.append(height)
    
    print(ans)

solution()