import sys

input = sys.stdin.readline

length = int(input())
answer = ''

def dfs(string, n):
    global answer

    if n > 1:
        for i in range(1, n // 2 + 1):
            if string[n-i:] == string[n-i-i:n-i]:
                return False

    if n == length:
        answer = string
        return True

    for i in ['1', '2', '3']:
        if dfs(string+i, n+1):
            return True

dfs('', 0)

print(answer)
