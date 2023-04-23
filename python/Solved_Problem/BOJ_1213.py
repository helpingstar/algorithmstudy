import sys
from collections import defaultdict

input = sys.stdin.readline

def solution():
    dic = defaultdict(int)
    word = input().rstrip()

    for c in word:
        dic[c] += 1

    n_odd = 0
    odd = -1
    for k, i in dic.items():
        if i % 2 == 1:
            n_odd += 1
            odd = k
        if n_odd > 1:
            return "I'm Sorry Hansoo"

    ans = ''

    for c in sorted(dic.keys()):
        ans += c * (dic[c] // 2)

    if n_odd:
        ans = ans + odd + ans[::-1]
    else:
        ans = ans + ans[::-1]
    return ans

print(solution())
