import sys

input = sys.stdin.readline

N, k = map(int, input().split())

is_prime = [True] * (N+1)

is_prime[0] = False
is_prime[1] = False

for i in range(2, N+1):
    if is_prime[i]:
        for j in range(i, N+1, i):
            if not is_prime[j]:
                continue
            is_prime[j] = False
            k -= 1
            if k == 0:
                print(j)

# print(is_prime)
