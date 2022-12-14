import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    tmp = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    if tmp > 0:
        return 1, 0
    elif tmp == 0:
        if min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= (max(y1, y2)):
            return 0, 1
        else:
            return 0, 0
    else:
        return -1, 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

v1, check1 = ccw(x1, y1, x2, y2, x3, y3)
v2, check2 = ccw(x1, y1, x2, y2, x4, y4)
v3, check3 = ccw(x3, y3, x4, y4, x1, y1)
v4, check4 = ccw(x3, y3, x4, y4, x2, y2)


if v1 * v2 * v3 * v4 == 0:
    if check1 or check2 or check3 or check4:
        print(1)
    else:
        print(0)
elif v1 * v2 < 0 and v3 * v4 < 0:
    print(1)
else:
    print(0)
