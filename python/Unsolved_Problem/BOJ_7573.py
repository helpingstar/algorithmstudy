import sys

input = sys.stdin.readline

N, L, F = map(int, input().split())

fishes = []

for _ in range(F):
    a, b = map(int, input().split())
    fishes.append((a, b))

ans = 1


def check(x, y):
    result = 0
    for w in range(1, N//2):
        count = 0
        h = N//2 - w

        for f_x, f_y in fishes:
            if x <= f_x <= x + h and y <= f_y <= y + w:
                count += 1

        result = max(result, count)

    return result


for i in range(F):
    for j in range(F):
        ans = max(ans, check(fishes[i][0], fishes[j][1]))


print(ans)
