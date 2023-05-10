import sys

input = sys.stdin.readline
"""
5 6 7 8 9 10
3 3 4 
"""


def solution():
    W, H = map(int, input().split())
    target = int(input())
    if W == H and target == W*H:
        print(W//2+1, H//2+1)
        return
    count = 0
    x = y = 0
    for i in range(1, min(W, H)+2, 2):
        if count + 2 * (W + H - 2 * i) >= target:
            x, y = i//2+1, i//2+1
            if target <= count + (H-i):
                print(x, y + target - count - 1)
                return

            y += (H-i)
            count += (H-i)

            if target <= count + (W-i):
                print(x + target - count - 1, y)
                return

            x += (W-i)
            count += (W-i)

            if target <= count + (H-i):
                print(x, y - (target - count - 1))
                return

            y -= (H-i)
            count += (H-i)

            print(x-(W-i-1), y)
            return
        count += 2 * (W + H - 2 * i)
    print(0)


solution()
