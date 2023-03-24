import sys

input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]
