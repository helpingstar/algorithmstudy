import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

sell = defaultdict(int)

ans_cnt = 0
result = ''
for _ in range(n):
    book = input().rstrip()
    sell[book] += 1
    if sell[book] > ans_cnt:
        result = book
        ans_cnt = sell[book]
    elif sell[book] == ans_cnt and book < result:
        result = book

print(result)