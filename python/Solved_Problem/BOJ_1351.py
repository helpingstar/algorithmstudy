import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def solution():
    N, P, Q = map(int, input().split())
    visit = {0: 1}
    def dp(num):
        if num in visit:
            return visit[num]
        
        visit[num // P] = dp(num // P)
        visit[num // Q] = dp(num // Q)
        return visit[num // P] + visit[num // Q]
    
    print(dp(N))

solution()
