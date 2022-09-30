import sys

input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    temp = input().rstrip()
    temp_set = set()
    flag = True
    prev = ''
    for c in temp:
        if c == prev:
            continue
        elif c in temp_set:
            flag = False
            break
        else:
            temp_set.add(c)
            prev = c
    if flag:
        ans += 1

print(ans)
