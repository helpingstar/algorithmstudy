import sys
from collections import defaultdict
from itertools import permutations
input = sys.stdin.readline

def n_count(origin, question):
    dic = defaultdict(list)

    for i in range(3):
        dic[origin % 10].append(i)
        dic[question % 10].append(i)

        origin //= 10
        question //= 10

    strike = ball = 0

    for k, v in dic.items():
        if len(v) == 2:
            if v[0] == v[1]:
                strike += 1
            else:
                ball += 1

    return (strike, ball)

def num_checker(num):
    for q, s, b in checker:
        if n_count(num, q) != (s, b):
            return False
    return True

checker = []
for _ in range(int(input())):
    q, s, b = map(int, input().split())
    checker.append((q, s, b))

answer = 0

for perm in permutations(range(1, 10), 3):
    num = perm[0] * 100 + perm[1] * 10 + perm[2]
    if num_checker(num):
        answer += 1

print(answer)
