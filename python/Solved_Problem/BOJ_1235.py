import sys

input = sys.stdin.readline


def check(length):
    check = set()
    for num in nums:
        if num[-length:] in check:
            return False
        check.add(num[-length:])

    return True


T = int(input())

nums = [input().rstrip() for _ in range(T)]

nums.sort()

for i in range(1, len(nums[0]) + 1):
    if check(i):
        print(i)
        break
