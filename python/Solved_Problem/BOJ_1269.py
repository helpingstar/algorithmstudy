import sys

input = sys.stdin.readline

n_a, n_b = map(int, input().split())

a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

print(len(a_set ^ b_set))
