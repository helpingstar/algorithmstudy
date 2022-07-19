import sys

input = sys.stdin.readline

def solution():
    n, k = input().rstrip().split()
    n_len = len(n)
    n, k = int(n), int(k)
    length = 0
    for i in range(1, n_len):
        length += (9*(10**(i-1)))*i
        n -= (9*(10**(i-1)))
    length += n_len * n

    if k > length:
        return -1
    
    k_len = 0
    for i in range(1, n_len):
        k_len += 1
        if k // ((9*(10**(i-1)))*i) == 0:
            break
        else:
            k -= ((9*(10**(i-1)))*i)

    k_len += 1

    quo = k // k_len
    mod = k % k_len

    k_len -= 1

    if mod == 0:
        return (10 ** k_len + quo - 1) % 10
    else:
        temp = (10**k_len + quo)
        for j in range(k_len-mod+1):
            temp //= 10
        return temp % 10

print(solution())