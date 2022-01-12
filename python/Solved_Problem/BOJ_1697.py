from collections import deque

n, k = map(int, input().split())

def fastest_time(n, k):
    if n >= k:
        return n - k
    pos = [100001] * 100001
    queue = deque()
    pos[n] = 0
    queue.append(n)
    while queue:
        t = queue.popleft()
        next_t = [t-1, t+1, 2*t]
        for nt in next_t:
            if not (0 <= nt <= 100000):
                continue
            if pos[nt] <= pos[t] + 1:
                continue
            queue.append(nt)
            pos[nt] = pos[t] + 1
    if pos[k] != 100001:
        return pos[k]

print(fastest_time(n, k))
            