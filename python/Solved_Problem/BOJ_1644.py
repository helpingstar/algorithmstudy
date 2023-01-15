import sys

input = sys.stdin.readline
def solution():
    n = int(input())

    check = [True] * (n+1)
    prime = []

    for i in range(2, n//2 + 1):
        check[2*i] = False

    for i in range(2, n//3 + 1):
        check[3*i] = False

    for i in range(2, n+1):
        if check[i]:
            prime.append(i)
            cnt = 2
            while i * cnt <= n:
                check[i*cnt] = False
                cnt += 1

    prime_sum = [0]

    for p in prime:
        prime_sum.append(p + prime_sum[-1])
    # print(prime_sum)
    l, r = 0, 1

    result = 0

    while l < r and r < len(prime_sum):
        tmp = prime_sum[r] - prime_sum[l]
        if tmp < n:
            r += 1
        elif tmp > n:
            l += 1
        else:
            result += 1
            l += 1
            r += 1
    print(result)

solution()
