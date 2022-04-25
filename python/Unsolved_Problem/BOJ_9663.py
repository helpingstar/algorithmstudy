import sys

input = sys.stdin.readline

n = int(input())
result = 0

def promising(n, list):
    if not list:
        return True
    for i, p in enumerate(list):
        if p == n:
            return False
        if p - n == i - len(list):
            return False
    return True


def queens(n, list):
    global result
    if promising(n, list):
        if len(list) == n:
            result += 1
        else:
            for i in range(1, n+1):
                queens(i, list)

queens(n, [])

print(result)