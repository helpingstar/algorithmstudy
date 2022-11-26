import sys
from collections import defaultdict

input = sys.stdin.readline

word = input().rstrip()
target = input().rstrip()
target_to_index = {char: idx for idx, char in enumerate(target)}

check = defaultdict(int)

for c in word:
    if c in target:
        if c == target[0]:
            check[c] += 1
        else:
            if check[target[target_to_index[c] - 1]] > check[c]:
                check[c] += 1

print(check[target[-1]])
