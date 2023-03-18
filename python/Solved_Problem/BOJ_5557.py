import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

check = [0] * 21
check[nums[0]] = 1

for num in nums[1:-1]:
    new_check = [0] * 21
    for i in range(num, 21):
        new_check[i] += check[i-num]
    for i in range(num, 21):
        new_check[i-num] += check[i]
    check = new_check

print(check[nums[-1]])
