import sys

input = sys.stdin.readline

a, b = map(int, input().split())

def lcd(a, b):
    b, a = max(a, b), min(a, b)
    if b % a == 0:
        return a
    else:
        return lcd(a, b-a)

lc = lcd(a, b)

print(lc)
print(a // lc * b)
