import sys

input = sys.stdin.readline


def solution():
    word = input().rstrip()

    def failure(pattern):
        result = 0
        table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[j] != pattern[i]:
                j = table[j - 1]

            if pattern[i] == pattern[j]:
                j += 1
                table[i] = j
                result = max(result, j)
        # print(table)
        return result

    ans = 0
    for i in range(len(word)):
        ans = max(ans, failure(word[i:]))
    print(ans)


solution()
