import sys

input = sys.stdin.readline


def solution():
    A, B = map(int, input().split())
    num = int(input())
    A_num = list(map(int, input().split()))

    number = 0

    for i, n in enumerate(reversed(A_num)):
        number += (A**i) * n

    result = []

    while number > 0:
        result.append(number % B)
        number //= B

    print(*reversed(result))


solution()
