import sys

input = sys.stdin.readline

N = int(input())

S = input().rstrip()
ans = -float('inf')

def cal(num1, op, num2):
    num1 = int(num1)
    num2 = int(num2)
    if op == '+':
        return num1 + num2
    elif op == '*':
        return num1 * num2
    else:
        return num1 - num2

def dp(idx, value):
    global ans

    if idx == N-1:
        ans = max(ans, value)

    if idx < N-2:
        dp(idx+2, cal(value, S[idx+1], S[idx+2]))

    if idx < N-4:
        dp(idx+4, cal(value, S[idx+1], cal(S[idx+2], S[idx+3], S[idx+4])))

dp(0, int(S[0]))

print(ans)
