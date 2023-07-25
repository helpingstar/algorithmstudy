import sys

input = sys.stdin.readline


def solution():
    number = input().rstrip()
    cnt = 0
    while len(number) > 1:
        cnt += 1
        new_number = 0
        for n in number:
            new_number += int(n)
        number = str(new_number)

    print(cnt)
    result = "YES" if int(number) in {3, 6, 9} else "NO"
    print(result)
    return


solution()
