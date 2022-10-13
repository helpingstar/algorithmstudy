n = int(input())
cur = 2
while n != 1:
    while n % cur == 0:
        print(cur)
        n //= cur
    cur += 1
