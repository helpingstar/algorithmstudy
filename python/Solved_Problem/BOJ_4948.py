import sys

input = sys.stdin.readline

is_prime = [1] * 246913
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, 246913):
    if is_prime[i] == 1:
        cnt = 2
        while cnt * i < 246913:
            is_prime[cnt * i] = 0
            cnt += 1

sum_prime = [0] * 246913
for i in range(1,246913):
    sum_prime[i] = sum_prime[i-1] + is_prime[i]

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(sum_prime[2*n] - sum_prime[n])
