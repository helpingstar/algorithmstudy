import sys

input = sys.stdin.readline

def solution():
    nums = [int(input()) for _ in range(8)]
    num_map = dict()
    for i in range(8):
        num_map[nums[i]] = i+1
        
    nums.sort(reverse=True)
    
    result = 0
    ans = []
    for i in range(5):
        result += nums[i]
        ans.append(num_map[nums[i]])
    ans.sort()
    
    print(result)
    print(*ans)

solution()