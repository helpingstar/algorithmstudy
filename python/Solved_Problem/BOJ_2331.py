import sys

input = sys.stdin.readline

check = []

a, p = map(int, input().split())
check.append(a)

while True:
    new_a = 0
    while a:
        new_a += (a % 10) ** p
        a //= 10

    if new_a in check:
        print(check.index(new_a))
        break
    check.append(new_a)
    a = new_a
