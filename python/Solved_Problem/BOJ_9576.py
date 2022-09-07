import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    
    checked = [False for _ in range(n+1)]
    rgs = [list(map(int, input().split())) for _ in range(m)]
    
    rgs.sort(key=lambda x: (x[1], x[0]))
    
    count = 0
    
    for start, end in rgs:
        # is_checked = False
        for cur in range(start, end+1):
            if not checked[cur]:
                checked[cur] = True
                # is_checked = True
                count += 1
                break
            
    print(count)