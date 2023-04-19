import sys

input = sys.stdin.readline

a_word, b_word = input().split()

def check_word(a_word, b_word):
    result = 0
    for i in range(len(a_word)):
        if a_word[i] != b_word[i]:
            result += 1

    return result
ans = float('inf')
for i in range(len(b_word) - len(a_word)+1):
    ans = min(ans, check_word(a_word, b_word[i: i+len(a_word)]))

print(ans)
