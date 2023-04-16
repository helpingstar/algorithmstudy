import sys

input = sys.stdin.readline

for _ in range(int(input())):
    press = input().rstrip()

    cur = 0
    word = []
    temp = []
    for c in press:
        if c in {'<', '>', '-'}:
            if temp:
                word = word[:cur] + temp + word[cur:]
                cur += len(temp)
                temp = []

            if c == '<':
                cur = max(0, cur-1)
            elif c == '>':
                cur = min(cur+1, len(word))
            else:
                word = word[:cur-1] + word[cur:]
        else:
            temp.append(c)

    word = word[:cur] + temp + word[cur:]
    print(''.join(word))
