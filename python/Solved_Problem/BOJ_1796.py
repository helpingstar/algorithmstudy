import sys

input = sys.stdin.readline


def solution():
    word = input().rstrip()
    checker = dict()
    for i, c in enumerate(word):
        if c not in checker:
            checker[c] = [i, i]
        else:
            checker[c][0] = min(checker[c][0], i)
            checker[c][1] = max(checker[c][1], i)
    # print(checker)
    dp = [len(word), len(word)]
    pos = [0, 0]
    for c in sorted(checker.keys()):
        l, r = checker[c]
        dist = checker[c][1] - checker[c][0]
        r_value = min(abs(pos[0] - l)+dp[0], abs(pos[1] - l)+dp[1]) + dist
        l_value = min(abs(pos[0] - r)+dp[0], abs(pos[1] - r)+dp[1]) + dist
        pos = [l, r]
        dp = [l_value, r_value]
    print(min(dp))


solution()
