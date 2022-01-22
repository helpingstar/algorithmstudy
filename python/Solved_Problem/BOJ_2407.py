import sys
input = sys.stdin.readline

n, r = map(int, input().split())
per_table = dict()
def combination(n, r):
    r = min(n-r, r)
    if (n, r) in per_table:
        return per_table[(n, r)]
    if r == 1:
        return n
    if r == 0:
        return 1
    per_table[(n, r)] = combination(n-1, r) + combination(n-1, r-1)
    return per_table[(n, r)]

print(combination(n, r))