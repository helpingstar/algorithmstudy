import sys
input = sys.stdin.readline

n = int(input())

if n % 4 in {1, 3}:
    print('SK')
else:
    print('CY')