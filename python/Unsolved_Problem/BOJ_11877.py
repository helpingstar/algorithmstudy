import sys

input = sys.stdin.readline

def solution():
    n, x = map(int, input().split())
    if ((n-2)*(n-1) // 2) < x:
        return -1
    
    if n < 3:
        return -1

    cnt = 0
    i = n-2
    while x != 0:
        if x - i <= 0:
            break
        
        x -= i
        cnt += 1
        i -= 1
    
    arr = [n]
    for i in range(1, 1+cnt):
        arr.append(i)
    # n-cnt-1개가 남는다.
    for i in range(n-1, cnt+1, -1):
        if i-1 == x:
            arr.append(cnt+1)
            arr.append(i)
            continue
        arr.append(i)

    print(*arr)

solution()
