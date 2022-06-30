"""
가장 적은 비행기 "종류"가 아니라
비행기 "횟수" 로 착각하여 MST가 아닌
TSP로 풀려고 했다.
"""

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    node, edge = map(int, input().split())
    for _ in range(edge):
        _ = input()
    print(node-1)