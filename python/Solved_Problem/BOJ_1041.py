import sys

input = sys.stdin.readline

def solution():
    n_size = int(input())
    dice = tuple(map(int, input().split()))

    if n_size == 1:
        print(sum(dice) - max(dice))
        return

    """
      3
    4 0 1 5
      2
    """

    points = ((0, 1, 2), (0, 2, 4), (0, 4, 3), (0, 3, 1), (5, 1, 2), (5, 2, 4), (5, 4, 3), (5, 3, 1))
    edges = ((0, 1), (0, 2), (0, 4), (0, 3), (3, 1), (1, 2), (2, 4), (4, 3), (5, 1), (5, 2), (5, 4), (5, 3))

    min_edges = min_points = float('inf')
    min_square = min(dice)
    for a, b, c in points:
        min_points = min(min_points, dice[a] + dice[b] + dice[c])
    
    for a, b in edges:
        min_edges = min(min_edges, dice[a] + dice[b])
    
    n_square = (n_size - 2) * (n_size - 2) + 4 * (n_size-2) * (n_size - 1)
    n_edges = 4 * (n_size - 1) + 4 * (n_size-2)
    n_point = 4
    # print(n_square, n_edges, n_point)
    print(min_edges * n_edges + min_points * n_point + min_square * n_square)

solution()