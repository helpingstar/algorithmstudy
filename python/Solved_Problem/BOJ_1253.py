import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

def solution():
    ans = 0
    if n < 3:
        return 0
    for i in range(0, n):
        if check(i):
            ans += 1
    return ans

def check(index):
    left = 1 if index == 0 else 0
    right = n-1 if index != n-1 else n-2
    num = nums[index]
    while left < right:
        temp = nums[left] + nums[right]
        if temp < num:
            left += 1
            if left == index:
                left += 1
        elif temp > num:
            right -= 1
            if right == index:
                right -=1
        else:
            return True
    return False

print(solution())