import sys
from itertools import combinations
from collections import defaultdict
input = sys.stdin.readline


def solution():
    T = int(input())

    def dist(a, b):
        distance = 0
        for i in range(4):
            if a[i] != b[i]:
                distance += 1
        return distance

    def get_result():
        n = int(input())
        mbtis = list(input().split())
        count = defaultdict(int)
        real_mbtis = []
        for mbti in mbtis:
            count[mbti] += 1
            if count[mbti] >= 3:
                return 0
            else:
                real_mbtis.append(mbti)
        L = len(real_mbtis)
        result = float('inf')
        for comb in combinations(range(L), 3):
            a, b, c = comb
            result = min(result, dist(
                real_mbtis[a], real_mbtis[b]) + dist(real_mbtis[b], real_mbtis[c]) + dist(real_mbtis[a], real_mbtis[c]))
        return result

    for _ in range(T):
        print(get_result())


solution()
