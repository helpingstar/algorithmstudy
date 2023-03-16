import sys

input = sys.stdin.readline

e, s, m = map(int, input().split())

cur = s

def get_num(num, a):
    temp = num % a
    if temp == 0:
        return a
    else:
        return temp

while True:
    if get_num(cur, 15) == e and get_num(cur, 19) == m:
        print(cur)
        break
    cur += 28
