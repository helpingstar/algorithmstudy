import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
mapper = defaultdict(int)
answer = 0
for _ in range(n):
    word = input().rstrip()
    for i, c in enumerate(word):
        mapper[c] += 10 ** (len(word) - i - 1)

print(sorted(mapper.items(), key=lambda x: (-x[1])))

cur = 9
for c, i in sorted(mapper.items(), key=lambda x: (-x[1])):
    answer += i * cur
    cur -= 1

print(answer)
