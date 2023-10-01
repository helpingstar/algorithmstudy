import sys
from collections import deque

input = sys.stdin.readline

def solution():
    word = input().rstrip()

    ans = 'z' * 51

    L = len(word)

    for i in range(1, L-1):
        for j in range(i+1, L):
            a = word[:i]
            b = word[i:j]
            c = word[j:]
            temp = a[::-1] + b[::-1] + c[::-1]
            
            if temp < ans:
                ans = temp
    print(ans)

solution()