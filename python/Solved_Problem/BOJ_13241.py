a, b = map(int, input().split())

def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    while a % b != 0:
        a = a - b
        if b > a:
            a, b = b, a
    return b

print(a // gcd(a, b) * b)