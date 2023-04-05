import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())

already = {'a', 'n', 't', 'i', 'c'}

words = []

for _ in range(N):
    word = set(input().rstrip()) - already
    word = ''.join(word)
    words.append(word)

if K < 5:
    print(0)
else:
    ans = 0

    all_alphabet = {chr(i) for i in range(ord('a'), ord('z') + 1)}
    all_alphabet -= already
    all_alphabet = sorted(list(all_alphabet))

    a2n = {alphabet: i for i, alphabet in enumerate(all_alphabet)}
    n_words = []
    for word in words:
        temp = 0
        temp += sum([1 << (a2n[c]+1) for c in word])
        n_words.append(temp)
    # print(all_alphabet)
    # print(a2n)
    # print(words)
    # print(n_words)
    for comb in combinations(range(1, len(all_alphabet) + 1), K-5):
        result = 0
        temp = 0
        for i in comb:
            temp += 1 << i

        for n_word in n_words:
            if n_word & temp == n_word:
                result += 1
        ans = max(ans, result)
    print(ans)
