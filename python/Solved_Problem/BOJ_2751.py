import sys

n = int(sys.stdin.readline())

li = [int(sys.stdin.readline()) for _ in range(n)]

li.sort()

for i in li:
    print(i)
    