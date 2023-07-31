import sys


def solution():
    input = sys.stdin.readline

    N = int(input())

    nums = list(map(int, input().split()))

    prime = [True] * 1_000_001
    prime[0] = prime[1] = False

    for i in range(2, int(1_000_001 ** 0.5) + 1):
        if prime[i]:
            for j in range(i*2, 1_000_001, i):
                prime[j] = False

    result = 1
    for n in nums:
        if prime[n] and result % n != 0:
            result *= n

    if result == 1:
        print(-1)
    else:
        print(result)


solution()
