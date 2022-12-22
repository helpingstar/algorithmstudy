import sys

input = sys.stdin.readline

t = int(input())

def solution():
    n = int(input())
    spot_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        spot_list.append((a, b))
        
    spot_list.sort()
    
    

for _ in range(t):
    solution()
    