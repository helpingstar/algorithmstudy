import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

if not m:
    print(min((len(str(n)), abs(100-n))))
else:
    crashed = set(map(int, input().split()))