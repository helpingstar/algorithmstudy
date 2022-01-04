n = int(input())
total = 0

if n < 25:
    total += (n // 5)
elif 25 <= n < 125:
    total += (n // 5)
    total += (n // 25)
else:
    total += (n // 5)
    total += (n // 25)
    total += (n // 125)

print(total)