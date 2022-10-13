n = int(input())

cur = 1

def divided_sum(num):
    result = num
    while num != 0:
        result += (num % 10)
        num //= 10
    return result

while True:
    if divided_sum(cur) == n:
        print(cur)
        break
    elif cur > n:
        print(0)
        break
    cur += 1
