import sys

input = sys.stdin.readline


def solution():
    sentence = input().rstrip()
    ucpc = ("U", "C", "P", "C")

    cur = 0
    clear = False

    for c in sentence:
        if c == ucpc[cur]:
            cur += 1
        if cur == 4:
            clear = True
            break

    if clear:
        print("I love UCPC")
    else:
        print("I hate UCPC")


solution()
