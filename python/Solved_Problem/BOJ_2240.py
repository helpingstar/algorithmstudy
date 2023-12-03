import sys

input = sys.stdin.readline


def solution():
    n_time, n_move = map(int, input().split())
    fruit = []
    prev_way = int(input())
    first = prev_way
    cnt = 1
    for _ in range(n_time - 1):
        way = int(input())
        if prev_way == way:
            cnt += 1
        else:
            fruit.append(cnt)
            cnt = 1
        prev_way = way
    fruit.append(cnt)
    # print(fruit)

    anchor = 1 & (first - 1)

    table = [[0] * (n_move + 1), [0] * (n_move + 1)]

    for i, n in enumerate(fruit):
        if (i + anchor) % 2 == 0:
            table[0][0] += n
            for m in range(1, n_move+1):
                table[0][m] = max(table[0][m], table[1][m-1]) + n
        else:
            if i != 0:
                table[1][0] += n
            for m in range(1, n_move+1):
                table[1][m] = max(table[1][m], table[0][m-1]) + n
    # print(table)
    print(max(max(table[0]), max(table[1])))
        

solution()
