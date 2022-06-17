"""
이분 탐색으로 풀었다.
어떤 A숫자와 차이가 M인 숫자중 가장 작은 숫자를 고르려면
정렬된 배열에서 A+M의 인덱스를 찾으면 된다. 해당 인덱스가 A의 인덱스보다 작거나
배열의 크기를 넘어갈 경우 더 이상 탐색할 필요가 없다.
"""


import sys
import bisect
input = sys.stdin.readline

n, diff = map(int, input().split())
nums = []

for _ in range(n):
    inum = int(input())
    nums.append(inum)

nums.sort()

ans = 10e9

for i in range(n):
    target = diff + nums[i]
    idx_tar = bisect.bisect_left(nums, target)
    if idx_tar < i or idx_tar >= n:
        break
    if nums[idx_tar] - nums[i] < ans:
        ans = nums[idx_tar] - nums[i]

print(ans)