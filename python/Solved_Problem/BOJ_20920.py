import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

counter = defaultdict(int)

all_word = set()

for _ in range(N):
    word = input().rstrip()

    if len(word) < M:
        continue

    all_word.add(word)

    counter[word] += 1

all_word = list(all_word)

all_word.sort(key=lambda x: (-counter[x], -len(x), x))

print(*all_word, sep='\n')
