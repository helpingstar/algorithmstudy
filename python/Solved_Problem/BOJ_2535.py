import sys

input = sys.stdin.readline


def solution():
    N = int(input())

    members = []

    for _ in range(N):
        a, b, c = map(int, input().split())
        members.append((a, b, c))

    members.sort(key=lambda x: x[2], reverse=True)
    nations = [0] * (N+1)
    medalist = []

    for a, b, c in members:
        if nations[a] >= 2:
            continue
        medalist.append((a, b))
        nations[a] += 1
        if len(medalist) == 3:
            break

    for medal in medalist:
        print(*medal)


solution()
