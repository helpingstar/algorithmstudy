import sys

input = sys.stdin.readline

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())



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

one = gcd(a1, b1)
two = gcd(a2, b2)

a1 //= one
b1 //= one
a2 //= two
b2 //= two

g = gcd(b1, b2)
l = b1 // g * b2 

a3 = a1 * b2 // g + a2 * b1 // g
b3 = l

three = gcd(a3, b3)

a3 //= three
b3 //= three

print(a3, b3)