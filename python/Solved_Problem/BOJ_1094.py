import sys

input = sys.stdin.readline

n = int(input())

print(sum(list(map(int, bin(n)[2:]))))