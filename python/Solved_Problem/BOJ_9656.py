import sys

input = sys.stdin.readline

n = int(input())

if n % 4 in {0, 2}:
    print('SK')
else:
    print('CY')
