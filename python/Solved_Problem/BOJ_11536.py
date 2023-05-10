import sys

input = sys.stdin.readline


def solution():
    T = int(input())
    names = [input().rstrip() for _ in range(T)]

    asc = True
    dsc = True

    for i in range(T-1):
        if names[i] > names[i+1]:
            asc = False
        else:
            dsc = False

    if asc:
        return 'INCREASING'

    if dsc:
        return 'DECREASING'

    return 'NEITHER'


print(solution())
