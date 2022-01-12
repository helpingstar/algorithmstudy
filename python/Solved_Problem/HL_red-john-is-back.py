n = int(input())

d = [0] * 41
d[1], d[2], d[3], d[4] = 1, 1, 1, 2

def get_prime_num(n):
    number = [1] * (n+1)
    number[0], number[1] = 0, 0
    for i in range(2, n + 1):
        if number[i]:
            for j in range(2, n // i + 1):
                number[i * j] = 0
    return sum(number)
            

for i in range(5, 41):
    d[i] = d[i-1] + d[i-4]    

for _ in range(n):
    print(get_prime_num(d[int(input())]))