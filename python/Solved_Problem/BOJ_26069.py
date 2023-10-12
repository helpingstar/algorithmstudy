import sys

input = sys.stdin.readline

def solution():
    T = int(input())
    dancing = set()
    dancing.add('ChongChong')
    for _ in range(T):
        a, b = input().split()
        if a in dancing or b in dancing:
            dancing.add(a)
            dancing.add(b)
    print(len(dancing))

solution()