import sys

input = sys.stdin.readline

for _ in range(int(input())):
    word = input().rstrip()
    side = int(len(word) ** 0.5)

    for c in range(side-1, -1, -1):
        for r in range(side):
            print(word[side*r + c], end='')
    print()
