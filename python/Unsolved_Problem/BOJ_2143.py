import sys
from collections import defaultdict

T = int(sys.stdin.readline())

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))
listB = list(map(int, sys.stdin.readline().split()))

dictA = defaultdict(int)


ans = 0

for i in range(a):
    for j in range(i, a, 1):
        dictA[sum(listA[i:j+1])] += 1

for i in range(b):
    for j in range(i, b, 1):
        ans += dictA[T - sum(listB[i:j+1])]

print(ans)