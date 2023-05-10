import sys

input = sys.stdin.readline
nums = []

while True:
    n = int(input())
    if n == 0:
        break
    nums.append(n)

n_max = max(nums)

is_prime = [True] * (n_max+1)

for i in range(2, int(n_max**0.5) + 1):
    if is_prime[i]:
        for j in range(2*i, n_max+1, i):
            if is_prime[j]:
                is_prime[j] = False

for num in nums:
    for i in range(2, num):
        if is_prime[i] and is_prime[num-i]:
            print(f'{num} = {i} + {num-i}')
            break
