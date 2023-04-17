import sys

input = sys.stdin.readline

x, y, c = map(float, input().split())


def get_c(x, y, w):
    h1 = (x**2 - w**2) ** 0.5
    h2 = (y**2 - w**2) ** 0.5

    w1 = w / (1 + h2/h1)
    # print(w1)
    p = w1 * y / w

    return (p ** 2 - w1 ** 2) ** 0.5


l, r = 0, min(x, y)

while True:
    mid = (l + r) / 2
    temp = get_c(x, y, mid)
    if abs(temp - c) < 0.0000001:
        print(mid)
        break

    if temp > c:
        l = mid
    else:
        r = mid
