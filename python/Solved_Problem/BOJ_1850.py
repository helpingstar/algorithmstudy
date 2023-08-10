import sys
import math

input = sys.stdin.readline


def solution():
    a, b = map(int, input().split())
    print('1'*(math.gcd(a, b)))


solution()
