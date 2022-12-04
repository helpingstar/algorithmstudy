import sys
from collections import deque

input = sys.stdin.readline


def solution():
    signal = input().rstrip()

    q = deque()
    q.append((signal, '100~1~'))
    q.append((signal, '01'))

    while q:
        signal, pattern = q.popleft()

        if not signal:
            if not pattern:
                return 'SUBMARINE'
            else:
                continue

        if not pattern:
            q.append((signal, '100~1~'))
            q.append((signal, '01'))
            continue

        if len(pattern) >= 2 and pattern[1] == '~':
            if signal[0] == pattern[0]:
                q.append((signal[1:], pattern[2:]))
                q.append((signal[1:], pattern))

        else:
            if signal[0] == pattern[0]:
                q.append((signal[1:], pattern[1:]))
    return 'NOISE   '

print(solution())
