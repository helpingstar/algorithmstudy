import sys

input = sys.stdin.readline

def solution():
    n, s, m = map(int, input().split())
    v = list(map(int, input().split()))
    q = {s}
    for i in range(n):
        nq = set()
        for now in q:
            if 0 <= (now - v[i]):
                nq.add(now-v[i])
            if (now + v[i]) <= m:
                nq.add(now+v[i])
        if not nq:
            return -1
        # print(nq)
        q = nq

    return max(q)

print(solution())
