import sys

input = sys.stdin.readline

n = int(input())

first = int(input())

window1 = [0, first, 0]
window2 = [0, 0, 0]
for _ in range(n-1):
    temp = int(input())
    window2 = [0, 0, 0]
    # print(window1)
    window2[0] = max(window1)
    window2[1], window2[2] = window1[0] + temp, window1[1] + temp
    # print(window2)
    window1 = window2

print(max(window1))
