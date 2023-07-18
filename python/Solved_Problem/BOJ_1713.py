import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    K = int(input())

    pics = dict()
    goods = list(map(int, input().split()))

    for i, g in enumerate(goods):
        if g in pics:
            pics[g][0] += 1
            continue

        # g not in pics
        if len(pics) >= N:
            lowest = 1001
            oldest = 1001
            picture = 1001
            for key, value in pics.items():
                if value[0] < lowest:
                    picture = key
                    lowest = value[0]
                    oldest = value[1]
                elif value[0] == lowest:
                    if value[1] < oldest:
                        picture = key
                        oldest = value[1]
            del pics[picture]
        pics[g] = [1, i]
    print(*sorted(pics.keys()))


solution()
