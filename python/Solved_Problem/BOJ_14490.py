import math
import sys


input = sys.stdin.readline

a, b = map(int, input().split(':'))

g = math.gcd(a, b)

print(a//g, b//g, sep=':')
