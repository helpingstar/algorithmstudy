import sys

input = sys.stdin.readline

def ten(n):
    five = 0
    cnt = 1

    while 5 ** cnt <= n:
        five += n // (5**cnt)
        cnt += 1
    two = 0
    cnt = 1
    while 2 ** cnt <= n:
        two += n // (2**cnt)
        cnt += 1

    return five, two

a, b = map(int, input().split())

a_f, a_t = ten(a)
b_f, b_t = ten(b)
a_b_f, a_b_t = ten(a-b)

f = a_f - b_f - a_b_f
t = a_t - b_t - a_b_t

print(min(f, t))
