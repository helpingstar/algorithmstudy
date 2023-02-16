import sys
input = sys.stdin.readline

n_number, n_change, n_mul = map(int, input().split())

nums = [int(input()) for _ in range(n_number)]

tree = [0] * (n_number)