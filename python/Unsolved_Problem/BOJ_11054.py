import sys
import bisect
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

asc_list = [1] * n
dsc_list = [1] * n
for i in range(n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            asc_list[i] = max(asc_list[i], asc_list[j] + 1)

n_list.reverse()
for i in range(n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            dsc_list[i] = max(dsc_list[i], dsc_list[j] + 1)


result = [asc_list[i] + dsc_list[n-i-1] for i in range(n)]
print(max(result)-1)