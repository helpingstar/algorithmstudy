import sys
import math
input = sys.stdin.readline

N = int(input())

switches = [-1] + list(map(int, input().split()))

for _ in range(int(input())):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, N+1, num):
            switches[i] = abs(switches[i] - 1)
    else:
        switches[num] = abs(switches[num] - 1)
        for i in range(1, N):
            if num - i == 0 or num + i == N+1:
                break
            if switches[num-i] == switches[num+i]:
                switches[num-i] = abs(switches[num-1]-1)
                switches[num+i] = abs(switches[num+1]-1)
    # print(switches)

for i in range(math.ceil(N / 20)):
    print(*switches[20*i+1: 20*i+21])
