import sys

input = sys.stdin.readline

nums = []

while True:
    num = int(input())
    if num == 0:
        break
    else:
        nums.append(num)

n_max = max(nums)

primes = [3]

is_prime = [True] * (n_max+1)

is_prime[0], is_prime[1] = False, False

for i in range(4, n_max+1, 2):
    is_prime[i] = False

for i in range(6, n_max+1, 3):
    is_prime[i] = False

for i in range(5, n_max+1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*2, n_max+1, i):
            is_prime[j] = False
# print(primes)
# print(nums)
for num in nums:
    l, r = 0, len(primes)-1
    while l <= r:
        if primes[l] + primes[r] == num:
            print(f'{num} = {primes[l]} + {primes[r]}')
            break
        elif primes[l] + primes[r] < num:
            l += 1
        else:
            r -= 1
