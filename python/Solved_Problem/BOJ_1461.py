import sys

input = sys.stdin.readline

n_book, n_hand = map(int, input().split())

minus = []
plus = []

books = list(map(int, input().split()))

for book in books:
    if book < 0:
        minus.append(-book)
    else:
        plus.append(book)
answer = 0

plus.sort()
minus.sort()
if minus and plus:
    book_max = max(minus[-1], plus[-1])
elif minus and not plus:
    book_max = minus[-1]
elif plus and not minus:
    book_max = plus[-1]

while len(plus) >= n_hand:
    answer += 2 * plus.pop()
    for _ in range(n_hand-1):
        plus.pop()

while len(minus) >= n_hand:
    answer += 2 * minus.pop()
    for _ in range(n_hand-1):
        minus.pop()

if plus:
    answer += 2 * plus[-1]
if minus:
    answer += 2 * minus[-1]

answer -= book_max

print(answer)
