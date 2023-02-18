import sys
import heapq
n = int(input())

nums = [int(input()) for _ in range(n)]

end_num = max(nums)

primes = [2, 3]

for i in range(5, end_num):
    if i % 2 == 0 or i % 3 == 0:
        continue
    is_prime = True
    for p in primes:
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
for num in nums:
    candidate = []
    l, r = 0, len(primes)-1
    while l <= r:
        if primes[l] + primes[r] == num:
            heapq.heappush(candidate, (primes[r] - primes[l], primes[l], primes[r]))
            l += 1
            r -= 1
        elif primes[l] + primes[r] < num:
            l += 1
        else:
            r -= 1
    print(candidate[0][1], candidate[0][2])