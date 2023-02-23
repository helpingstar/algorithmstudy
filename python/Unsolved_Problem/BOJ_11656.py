import sys

input = sys.stdin.readline

result = []

word = input().rstrip()

for i in range(len(word)):
    result.append(word[i:])
    
result.sort()

print(*result, sep='\n')