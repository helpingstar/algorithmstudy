import sys

input = sys.stdin.readline

a, b = map(int, input().split())

a_set = set(map(int, input().split()))

b_set = set(map(int, input().split()))


result = a_set - b_set

if len(result) == 0:
    print(0)
else:
    print(len(result))
    print(*sorted(list(result)))
