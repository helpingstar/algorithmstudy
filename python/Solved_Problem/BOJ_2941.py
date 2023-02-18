import sys

input = sys.stdin.readline

cnt = 0
word = input().rstrip()

cur = len(word) - 1

while cur >= 0:
    if word[cur] == '=':
        if word[cur-1] in {'c', 's'}:
            cur -= 2
        else: # z
            if word[cur-2] == 'd':
                cur -= 3
            else:
                cur -= 2
    elif word[cur] == '-':
        cur -= 2
    elif word[cur] == 'j':
        if word[cur-1] in {'l', 'n'}:
            cur -= 2
        else:
            cur -= 1
    else:
        cur -= 1
    cnt += 1

print(cnt)