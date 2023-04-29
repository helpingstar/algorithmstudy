import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

word = input().rstrip()

word_dic = defaultdict(int)

for c in word:
    word_dic[c] += 1

answer = 0

for _ in range(N-1):
    temp = input().rstrip()
    temp_dic = defaultdict(int)
    for c in temp:
        temp_dic[c] += 1

    all_keys = set()
    all_keys |= set(word_dic.keys())
    all_keys |= set(temp_dic.keys())

    diff = 0
    zero_count = [0, 0]
    for c in all_keys:
        diff += abs(word_dic[c] - temp_dic[c])
        if word_dic[c] == 1 and temp_dic[c] == 0:
            zero_count[0] += 1
        elif word_dic[c] == 0 and temp_dic[c] == 1:
            zero_count[1] += 1

    if diff <= 1:
        answer += 1
    else:
        if diff == 2 and zero_count == [1, 1]:
            answer += 1

print(answer)
