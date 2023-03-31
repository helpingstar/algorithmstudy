import sys
from collections import deque

ans = ''

sentence = input().rstrip()

opened = False
temp = ''

for c in sentence:
    # print(c)
    if c == '<':
        ans += temp[::-1]
        temp = ''
        ans += c
        opened = True
    elif c == '>':
        ans += temp + '>'
        opened = False
    elif c == ' ':
        if opened:
            ans += c
        else:
            ans += temp[::-1] + ' '
            temp = ''
    else:
        if opened:
            ans += c
        else:
            temp += c

ans += temp[::-1]

print(ans)
