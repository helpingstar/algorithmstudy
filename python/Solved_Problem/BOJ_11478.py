import sys

input = sys.stdin.readline

word = input().rstrip()
ans = set()
for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        ans.add(word[i:j])

print(len(ans))
