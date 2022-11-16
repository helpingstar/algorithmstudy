import sys

input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def ccw(x1, y1, x2, y2, x3, y3):
    if x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3 < 0:
        return -1
    else:
        return 1

if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) + ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == -2:
    print(1)
else:
    print(0)
