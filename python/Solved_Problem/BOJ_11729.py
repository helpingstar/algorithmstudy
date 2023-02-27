import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())

def hanoi(count, start, end):
    if count == 0:
        return
    hanoi(count-1, start, 6 - start - end)
    print(start, end)
    hanoi(count-1, 6 - start - end, end)
print(2**n-1)
hanoi(n, 1, 3)