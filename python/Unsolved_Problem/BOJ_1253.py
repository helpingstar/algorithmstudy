import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
numset = set(nums)
answer = set()

def solution():
    if n == 1:
        return 0
    l, r = 0, 1
    while l < r and r < n:
        if nums[l] + nums[r] in numset and nums[l] != nums[r]:
            if (nums[l] == 0 and nums[r] != nums[r+1]):
                pass
            else:
                answer.add((l, r))
        if r == n-1:
            l += 1
        elif l + 1 == r:
            r += 1
        elif nums[l+1] - nums[l] < nums[r+1] - nums[r]:
            l += 1
        else:
            r += 1
    return len(answer)

print(solution())

