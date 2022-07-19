import sys

input = sys.stdin.readline

n = int(input())
desc_list = []

def dp(length, num, cnt):
    if cnt == length:
        desc_list.append(num)
    else:
        for i in range(0, num%10):
            dp(length, num*10+i, cnt+1)

def bt(length):
    for i in range(10):
        dp(length, i, 1)

for i in range(1, 11):
    bt(i)

len_desc = len(desc_list)
if n >= len_desc:
    print(-1)
else:
    print(desc_list[n])