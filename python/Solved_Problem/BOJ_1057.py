import sys

input = sys.stdin.readline


def solution():
    N, t1, t2 = map(int, input().split())
    t1, t2 = sorted((t1, t2))
    members = [(i, i) for i in range(1, N+1)]

    cnt = 0
    while True:
        cnt += 1
        new_members = []
        for i in range(0, len(members), 2):
            if i == len(members) - 1 and len(members) % 2 == 1:
                start, end = members[i][0], members[i][1]
            else:
                start, end = members[i][0], members[i+1][1]

            new_members.append((start, end))
            if start <= t1 and t2 <= end:
                return cnt
        members = new_members


print(solution())
