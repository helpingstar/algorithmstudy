import sys

def solution():
    input = sys.stdin.readline

    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    lines.sort(key=lambda x: (x[0], -x[1]))

    if N == 1:
        print(lines[0][1] - lines[0][0])
        return

    result = 0
    a, b = lines[0]
    for s, e in lines[1:]:
        if b < s:
            result += (b - a)
            a, b = s, e
        else:
            if b < e:
                b = e
    result += (b - a)
    print(result)

solution()
