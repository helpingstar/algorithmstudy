import sys
from collections import deque
input = sys.stdin.readline


def solution():
    dx = (-1, -1, -1, 0, 0, 1, 1, 1)
    dy = (-1, 0, 1, -1, 1, -1, 0, 1)

    SIZE, n_tree, n_year = map(int, input().split())
    nutrition = [list(map(int, input().split())) for _ in range(SIZE)]

    trees = [[deque() for _ in range(SIZE)] for _ in range(SIZE)]

    tree_list = []
    for _ in range(n_tree):
        x, y, z = map(int, input().split())
        tree_list.append((z, x-1, y-1))
    tree_list.sort()

    for z, x, y in tree_list:
        trees[x][y].append(z)

    board = [[5] * SIZE for _ in range(SIZE)]

    for i in range(n_year):
        new_trees = [[deque() for _ in range(SIZE)] for _ in range(SIZE)]
        parent_trees = []
        # spring
        for x in range(SIZE):
            for y in range(SIZE):
                if trees[x][y]:
                    for i, z in enumerate(trees[x][y]):
                        if board[x][y] >= z:
                            board[x][y] -= z
                            new_trees[x][y].append(z+1)
                            if (z+1) % 5 == 0:
                                parent_trees.append((z+1, x, y))
                        else:
                            for k in range(i, len(trees[x][y])):
                                board[x][y] += trees[x][y][k] // 2
                            break

        # fall
        for z, x, y in parent_trees:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < SIZE and 0 <= ny < SIZE):
                    continue
                new_trees[nx][ny].appendleft(1)
        # winter
        for x in range(SIZE):
            for y in range(SIZE):
                board[x][y] += nutrition[x][y]

        trees = new_trees

    result = 0
    for x in range(SIZE):
        for y in range(SIZE):
            result += len(trees[x][y])
    return result


print(solution())
