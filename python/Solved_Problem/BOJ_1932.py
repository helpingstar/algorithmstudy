import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(int(input()))
elif n == 2:
    n1 = int(input())
    n21, n22 = map(int, input().split())
    print(max(n21, n22) + n1)
else:
    n1 = int(input())
    n21, n22 = map(int, input().split())
    high = [n1 + n21, n1 + n22]
    for i in range(1, n-1):
        line = list(map(int, input().split()))
        temp = []
        temp.append(high[0] + line[0])
        for j in range(i):
            temp.append(max(high[j], high[j+1]) + line[j+1])
        temp.append(high[-1] + line[-1])
        high = temp
    print(max(high))
    