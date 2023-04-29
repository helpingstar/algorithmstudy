import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())



def check(a):
    temp = defaultdict(int)
    while a != 1:
        for i in primes:
            while a % i == 0:
                a //= i
                temp[i] += 1

    for k, v in sorted(temp.items()):
        print(k, v)

nums = [int(input()) for _ in range(N)]
nums_r = max(nums)

is_prime = [True] * (int(nums_r ** 0.5) + 1)
is_prime[0], is_prime[1] = False, False
primes = []

for i in range(2, int(nums_r ** 0.5) + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*2, len(is_prime), i):
            is_prime[j] = False

for num in nums:
    check(num)
