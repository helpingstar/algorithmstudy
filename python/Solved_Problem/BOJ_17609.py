import sys
from collections import deque

input = sys.stdin.readline


def solution():
    T = int(input())

    for _ in range(T):
        word = input().rstrip()
        what = 2
        q = deque()
        q.append((0, len(word) - 1, 1))
        while q:
            l, r, c = q.popleft()
            if l >= r:
                if c == 1:
                    what = 0
                elif c == 0:
                    what = 1
            else:
                if word[l] == word[r]:
                    q.append((l + 1, r - 1, c))
                else:
                    if c > 0:
                        q.append((l + 1, r, 0))
                        q.append((l, r - 1, 0))
                    else:
                        continue
        print(what)


solution()
