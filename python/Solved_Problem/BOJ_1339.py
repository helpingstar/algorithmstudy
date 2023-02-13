import sys
from collections import defaultdict

input = sys.stdin.readline

alphabet = defaultdict(int)
n = int(input())

for _ in range(n):
    word = input().rstrip()
    length = len(word)
    for i in range(length):
        alphabet[word[length - i - 1]] += 10 ** i

alphabet_list = sorted(list(alphabet.items()), key=lambda x: -x[1])
ans = 0
cnt = 9
for _, num in alphabet_list:
    ans += num * cnt
    cnt -= 1
print(ans)
