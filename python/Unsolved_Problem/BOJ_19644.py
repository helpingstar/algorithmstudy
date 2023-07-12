import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    L = int(input())
    ML, MK = map(int, input().split())
    C = int(input())
    Z = [int(input()) for _ in range(L)]
    q = deque()
    cnt = 0
    answer = True

    for i in range(min(ML, L)):
        if cnt == 0:
            if Z[i]-MK*(i+1) <= 0:
                q.append(0)
            else:
                q.append(Z[i]-MK*(i+1))
                cnt += 1
        else:
            if Z[i]-MK*(i+1-cnt) <= 0:
                q.append(0)
            else:
                q.append(Z[i] - MK*(i+1-cnt))
                cnt += 1
    for i in range(ML, L):
        if q[0] == 0:
            q.popleft()
            if Z[i]-MK*(ML-cnt) <= 0:
                q.append(0)
            else:
                q.append(Z[i]-MK*(ML-cnt))
                cnt += 1
        else:
            q.popleft()
            if C > 0:
                C -= 1
            else:
                return "NO"

            if Z[i] - MK*(ML-cnt) <= 0:
                q.append(0)
                cnt -= 1
            else:
                q.append(Z[i] - MK * (ML-cnt))
    while q:
        if q[0] == 0:
            q.popleft()
        else:
            q.popleft()
            cnt -= 1
            if C > 0:
                C -= 1
            else:
                return "NO"
    return "YES"

print(solution())
