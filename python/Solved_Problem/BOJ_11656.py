import sys


def solution():
    input = sys.stdin.readline
    word = input().rstrip()

    ans = []
    for i in range(len(word)):
        ans.append(word[i:])
    print(*sorted(ans), sep='\n')


solution()
