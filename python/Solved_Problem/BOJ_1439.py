import sys

input = sys.stdin.readline

def solution():
    num = input().rstrip()
    if len(num) <= 1:
        return 0
    cnt = 0
    for i in range(len(num) - 1):
        if num[i] != num[i+1]:
            cnt += 1
    return (cnt-1)//2+1


print(solution())
