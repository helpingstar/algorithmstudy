import sys

input = sys.stdin.readline

def has_666(string):
    count = 0
    for c in string:
        if c == '6':
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False

n = int(input())

num = 0
cnt = 0
while True:
    num += 1
    s_num = str(num)
    if has_666(s_num):
        cnt += 1
        if cnt == n:
            print(s_num)
            break
