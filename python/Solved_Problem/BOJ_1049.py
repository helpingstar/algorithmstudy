import sys

input = sys.stdin.readline

n_need, n_brand = map(int, input().split())

min_six = min_one = 100000

for _ in range(n_brand):
    pkg, one = map(int, input().split())
    min_six = min(pkg, min_six, one*6)
    min_one = min(min_one, one)

ans = 0

while n_need > 0:
    if n_need >= 6:
        ans += min_six
        n_need -= 6
    else:
        ans += min(min_one * n_need, min_six)
        n_need = 0

print(ans)
