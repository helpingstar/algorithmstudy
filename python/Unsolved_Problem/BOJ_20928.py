import sys


def solution():
    input = sys.stdin.readline
    N, goal = map(int, input().split())
    pos = list(map(int, input().split()))
    step = list(map(int, input().split()))

    roads = [(pos[i], pos[i] + step[i]) for i in range(N)]

    cnt = 0
    limit = pos[0] + step[0]
    next_ = 0

    if goal <= limit:
        return 0

    for s, e in roads:
        if s <= limit:
            next_ = max(e, next_)
        else:
            if goal <= next_:
                return cnt + 1

            if s <= next_:
                limit = next_
                cnt += 1
                next_ = e
            else:
                return -1

    if goal <= next_:
        return cnt + 1

    return -1


if __name__ == "__main__":
    print(solution())
