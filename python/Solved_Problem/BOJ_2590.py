import sys
import math
input = sys.stdin.readline

papers = [0] + [int(input()) for _ in range(6)]

ans = papers[6]

while papers[5]:
    area = 36 - 5 * 5
    papers[5] -= 1
    papers[1] = max(0, papers[1] - area)
    ans += 1

while papers[4]:
    area = 36 - 4 * 4
    papers[4] -= 1

    area -= min(papers[2], 5) * 4
    papers[2] = max(0, papers[2] - 5)

    papers[1] = max(0, papers[1] - area)
    ans += 1

while papers[3]:
    if papers[3] >= 4:
        papers[3] -= 4
        area = 0
    elif papers[3] == 3:
        area = 36 - papers[3] * 9
        papers[3] -= 3

        area -= min(papers[2], 1) * 4
        papers[2] = max(papers[2] - 1, 0)
    elif papers[3] == 2:
        area = 36 - papers[3] * 9
        papers[3] -= 2

        area -= min(papers[2], 3) * 4
        papers[2] = max(papers[2] - 3, 0)
    else:
        area = 36 - papers[3] * 9
        papers[3] -= 1

        area -= min(papers[2], 5) * 4
        papers[2] = max(papers[2] - 5, 0)
    papers[1] = max(0, papers[1] - area)
    ans += 1

while papers[2]:
    area = 36 - min(papers[2], 9) * 4
    papers[2] = max(papers[2] - 9, 0)

    papers[1] = max(0, papers[1] - area)
    ans += 1

ans += math.ceil(papers[1] / 36)

print(ans)
