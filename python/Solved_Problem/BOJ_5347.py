import sys
import math

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    print(a // g * b)
