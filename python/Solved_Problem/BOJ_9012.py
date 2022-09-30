import sys

input = sys.stdin.readline

N = int(input())

def valid(string):
    ans = 0
    for c in string:
        if c == '(':
            ans += 1
        else:
            ans -= 1
            if ans < 0:
                return False
    if ans == 0:
        return True
    else:
        return False

for _ in range(N):
    if valid(input().rstrip()):
        print("YES")
    else:
        print("NO")
