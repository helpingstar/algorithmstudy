import sys

input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, input().split()))

temp = sum(nums[:K])
answer = temp

for i in range(K, N):
    # print(temp)
    temp += nums[i]
    temp -= nums[i-K]
    answer = max(temp, answer)
print(answer)
