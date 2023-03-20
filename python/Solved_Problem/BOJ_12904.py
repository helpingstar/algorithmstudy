import sys

input = sys.stdin.readline

start = list(input().rstrip())
target = list(input().rstrip())

while target:
    if start == target:
        print(1)
        break
    if target[-1] == 'A':
        target.pop()
    else:
        target.pop()
        target = list(reversed(target))

    if len(target) == len(start):
        if target == start:
            print(1)
            break
        else:
            print(0)
            break
