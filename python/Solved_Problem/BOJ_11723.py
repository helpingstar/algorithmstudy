import sys

input = sys.stdin.readline

s = set()
n = int(input())

for _ in range(n):
    op = input().rstrip()
    if op == 'all':
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif op == 'empty':
        s = set()
    else:
        do, num = op.split()
        num = int(num)
        
        if do == 'add':
            if num in s:
                continue
            s.add(num)
        elif do == 'remove':
            if num not in s:
                continue
            s.discard(num)
        elif do == 'check':
            print(1 if num in s else 0)
        else:
            if num in s:
                s.discard(num)
            else:
                s.add(num)