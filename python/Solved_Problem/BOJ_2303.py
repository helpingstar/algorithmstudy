import sys
from itertools import combinations
input = sys.stdin.readline


def solution():
    N = int(input())

    result = 0
    winner = 0
    for i in range(N):
        max_number = 0
        numbers = list(map(int, input().split()))
        for comb in combinations(numbers, 3):
            max_number = max(max_number, sum(comb) % 10)
        if result <= max_number:
            result = max_number
            winner = i + 1

    return winner


print(solution())
