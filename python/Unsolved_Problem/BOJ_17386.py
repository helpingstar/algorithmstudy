import sys

input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def outer_product(x1, y1, x2, y2, x3, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

if outer_product(x1, y1, x2, y2, x3, y3) * outer_product(x1, y1, x2, y2, x4, y4) < 0:
    print(1)
else:
    print(0)