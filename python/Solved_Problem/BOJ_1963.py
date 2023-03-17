import sys
from collections import defaultdict, deque

input = sys.stdin.readline

prime_map = defaultdict(list)

primes = [True] * 10000
primes[0] = primes[1] = False

for i in range(1, 10000):
    if primes[i]:
        if i > 1000:
            temp = str(i)
            for i in range(4):
                prime_map[temp[:i] + '-' + temp[i+1:]].append(temp)
        for j in range(2*i, 10000, i):
            primes[j] = False

def solution(start, end):
    if start == end:
        return 0

    q = deque()
    visited = set()
    q.append((start, 0))

    while q:
        now, cnt = q.popleft()
        for i in range(4):
            now_ = now[:i] + '-' + now[i+1:]
            for nxt in prime_map[now_]:
                if nxt in visited:
                    continue
                if nxt == end:
                    return cnt + 1
                q.append((nxt, cnt+1))
                visited.add(nxt)
    return "impossible"

N = int(input())
for _ in range(N):
    a, b = input().split()
    print(solution(a, b))
