import sys

input = sys.stdin.readline

def solution():
    T = int(input())
    
    nums = [int(input()) for _ in range(T)]
    
    max_num = max(nums)
    
    sum_list = [0] * (max_num + 1)
    
    for i in range(1, max_num + 1):
        for j in range(i, max_num+1, i):
            sum_list[j] += i
    
    sum_sum_list = [0] * (max_num + 1)
    
    for i in range(1, max_num + 1):
        sum_sum_list[i] = sum_list[i] + sum_sum_list[i-1]
    
    for num in nums:
        print(sum_sum_list[num])
        
solution()