import sys

input = sys.stdin.readline

n_num, n_size = map(int, input().split())
nums = list(map(int, input().split()))

max_num = max(nums)
min_num = min(nums)


def check(diff):
    t_min = 10001
    t_max = 0
    cnt = 1
    for num in nums:
        t_min = min(t_min, num)
        t_max = max(t_max, num)
        if t_max - t_min > diff:
            cnt += 1
            if cnt > n_size:
                return False
            t_min = num
            t_max = num
    return True


l, r = 0, max_num - min_num
ans = -1
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
