import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    clients = list(map(int, input().split()))

    print(len(clients) - len(set(clients)))


solution()
