import sys
import bisect
from itertools import permutations


def solution():
    input = sys.stdin.readline

    num1, num2 = input().split()

    num1 = tuple(map(int, num1))
    num2 = int(num2)

    combis = []
    for comb in sorted(list(permutations(num1, len(num1)))):
        combis.append(int("".join(map(str, comb))))

    index = bisect.bisect_right(combis, num2) - 1

    if index == -1:
        return -1
    elif index == len(combis) - 1 and combis[index] >= num2:
        return -1
    elif index == 0 and combis[index] >= num2:
        return -1
    elif len(str(combis[index])) < len(num1):
        return -1

    return combis[index]


print(solution())
