import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    words = [input().rstrip() for _ in range(n)]
    words.sort()
    available = True
    for i in range(n-1):
        if words[i+1][:len(words[i])] == words[i]:
            available = False
            break

    if available:
        print('YES')
    else:
        print('NO')
