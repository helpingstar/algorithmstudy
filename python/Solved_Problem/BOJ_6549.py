import sys
from collections import deque

input = sys.stdin.readline


def solution(nums: list):
    N = nums.pop(0)
    stack = deque()
    ans = 0
    for i in range(N):
        if not stack:
            stack.append(i)
            continue
        while stack and nums[stack[-1]] > nums[i]:
            tmp = stack.pop()
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            ans = max(ans, width * nums[tmp])
        stack.append(i)

    while stack:
        tmp = stack.pop()

        if not stack:
            width = N
        else:
            width = N - stack[-1] - 1
        ans = max(ans, width * nums[tmp])

    return ans


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    else:
        print(solution(nums))
