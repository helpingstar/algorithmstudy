import sys

def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    positions = [0] * 100_001
    
    for n in nums:
        positions[n] += 1
    
    dist = sum(nums)
    min_dist = dist
    left = 0
    right = len(nums)
    
    ans = -1
    
    for i in range(min(nums), max(nums) + 1):
        dist -= right
        dist += left
        right -= positions[i]
        left += positions[i]
        
        if dist < min_dist:
            ans = i
            min_dist = dist
    print(ans)

solution()
        