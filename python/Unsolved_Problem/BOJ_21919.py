import sys


input = sys.stdin.readline
N = int(input())
is_prime = [True] * 1000001
is_prime[0], is_prime[1] = False, False
for i in range(2, 1001):
    if is_prime[i]:
        for j in range(i*2, 1000001, i):
            is_prime[j] = False

nums = list(map(int, input().split()))

result = 1

for num in nums:
    if is_prime[num]:
        result *= num

if result == 1:
    print(-1)
else:
    print(result)
