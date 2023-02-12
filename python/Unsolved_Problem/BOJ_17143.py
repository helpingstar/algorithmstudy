import sys

input = sys.stdin.readline

n_row, n_col, n_shark = map(int, input().split())
shark_set = set()



for _ in range(n_shark):
    r, c, s, d, z = map(int, input().split())
    shark_set.add((r, c, s, d, z))

def next_shark_pos(r, c, s, d):
