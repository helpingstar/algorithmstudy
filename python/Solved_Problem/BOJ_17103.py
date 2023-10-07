import sys

input = sys.stdin.readline

def solution():
    T = int(input())

    nums = [int(input()) for _ in range(T)]
    n_max = max(nums)

    is_prime = [True] * n_max

    is_prime[0] = False
    is_prime[1] = False

    for i in range(4, n_max, 2):
        is_prime[i] = False
    for i in range(6, n_max, 3):
        is_prime[i] = False
    
    for i in range(5, int(n_max ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, n_max, i):
                is_prime[j] = False
    
    for n in nums:
        cnt = 0
        for i in range(n//2 + 1):
            if is_prime[i] and is_prime[n-i]:
                cnt += 1
        print(cnt)

solution()