import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]

pos = dict()

for r in range(5):
    for c in range(5):
        pos[board[r][c]] = (r, c)

nums = []

hor = [5] * 5
ver = [5] * 5
# dia[0] : /, dia[1]: \
dia = [5] * 2

for _ in range(5):
    nums += list(map(int, input().split()))

bingo = 0

for i, num in enumerate(nums):
    r, c = pos[num]
    hor[r] -= 1
    ver[c] -= 1
    if hor[r] == 0:
        bingo += 1
    if ver[c] == 0:
        bingo += 1

    if r == c:
        dia[1] -= 1
        if dia[1] == 0:
            bingo += 1

    if r + c == 4:
        dia[0] -= 1
        if dia[0] == 0:
            bingo += 1

    if bingo >= 3:
        print(i+1)
        break

# print(hor)
# print(ver)
# print(dia[0])
# print(dia[1])
# print(bingo)
