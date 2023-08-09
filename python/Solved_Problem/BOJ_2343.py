import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    left = 0
    right = sum(nums)

    def check(mid):
        nonlocal nums
        nonlocal M
        sum_ = 0
        cnt = 1
        for num in nums:
            if num > mid:
                return False
            sum_ += num
            if sum_ > mid:
                cnt += 1
                if cnt > M:
                    return False
                sum_ = num
        return True
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)


solution()
