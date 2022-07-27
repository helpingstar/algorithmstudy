import sys

input = sys.stdin.readline

n = int(input())
ans = 0
table = [-1] * n

def promising(x):
    for i in range(x):
        if table[i] == table[x] or (x+table[x]) == (i+table[i]) or (i-table[i]) == (x-table[x]):
            return False
    return True
    
def dp(cnt):
    global ans
    if cnt == n:
        ans += 1
        return
    else:
        for i in range(n):
            table[cnt] = i
            if promising(cnt):
                dp(cnt+1)
                
dp(0)
print(ans)