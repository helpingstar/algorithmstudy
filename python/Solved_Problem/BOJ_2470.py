import sys

input = sys.stdin.readline

n = int(input())

liquid = list(map(int, input().split()))

l, r = 0, n-1

liquid.sort()

result = 3000000000
r_l, r_r = -1, -1
while l < r:
    if liquid[l] + liquid[r] == 0:
        r_l, r_r = l, r
        break
    if abs(liquid[l] + liquid[r]) < result:
        r_l, r_r = l, r
        result = abs(liquid[l] + liquid[r])
    if liquid[l] + liquid[r] < 0:
        l += 1
    else:
        r -= 1

print(liquid[r_l], liquid[r_r])
