import sys

input = sys.stdin.readline

stick = input().rstrip()

num = 0
result = 0

cur = 0
while cur < len(stick):
    if stick[cur] == '(':
        if stick[cur+1] == ')':
            result += num
            cur += 1
        else:
            num += 1
        cur += 1
    else:
        num -= 1
        cur += 1
        result += 1

print(result)
    