import sys

input = sys.stdin.readline

m, n = map(int, input().split())

is_sosu = [True for _ in range(n+1)]

is_sosu[1] = False

for i in range(4, n+1, 2):
    is_sosu[i] = False
    
for i in range(6, n+1, 3):
    is_sosu[i] = False
    
for i in range(5, m+1):
    if is_sosu[i]:
        for j in range(i*2, n+1, i):
            is_sosu[j] = False
            
for i in range(m, n+1):
    if is_sosu[i]:
        print(i)
        for j in range(i*2, n+1, i):
            is_sosu[j] = False
