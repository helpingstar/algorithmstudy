import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = [i for i in range(1, n+1)]
can_get = [True] * n
ans = []
cnt = 0
cur = 0
temp = k
while cnt < n:
    # print(cur)
    if can_get[cur]:
        temp -= 1
        if temp == 0:
            ans.append(nums[cur])
            can_get[cur] = False
            temp = k
            cnt += 1
    cur = (cur+1) % n
print('<', end='')
print(*ans, sep=', ', end='')
print('>')
