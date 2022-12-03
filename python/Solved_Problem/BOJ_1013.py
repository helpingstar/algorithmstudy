import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

def check(signal):
    q = deque()
    q.append((signal, '100+1+'))
    q.append((signal, '01'))
    while q:
        now, pattern = q.popleft()
        # print(f'[debug]  q : {q}')
        # print(f'[debug]  now : {now}')
        # print(f'[debug]  pattern: {pattern}')
        if not now:
            if not pattern:
                return 'YES'
            continue
        if not pattern:
            q.append((now, '100+1+'))
            q.append((now, '01'))
            continue
        if len(pattern) >= 2 and pattern[1] == '+':
            if now[0] == pattern[0]:
                q.append((now[1:], pattern))
                q.append((now[1:], pattern[2:]))
        elif now[0] == pattern[0]:
            q.append((now[1:], pattern[1:]))
    return 'NO'

for _ in range(n):
    signal = input().rstrip()
    print(check(signal))
