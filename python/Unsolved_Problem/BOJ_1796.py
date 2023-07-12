'''
어차피 모두 엔터하니까 엔터 횟수는 중간에 굳이 카운트 할 필요 없음

1. 큐로 풀었더니 메모리 초과
'''

import sys
from collections import deque

input = sys.stdin.readline

def solution():
    word = input().rstrip()

    chars = dict()

    for i, c in enumerate(word):
        if c not in chars:
            chars[c] = [51, 0]

        chars[c][0] = min(chars[c][0], i)
        chars[c][1] = max(chars[c][1], i)

    order = sorted(chars.keys())

    # left, right
    steps = [len(word), len(word)]
    prev_l, prev_r = 0, 0
    for c in order:
        dist = chars[c][1] - chars[c][0]
        # go_XXX : XXX를 먼저 방문하고 XXX의 반대방향을 방문
        go_left = min(steps[0] + abs(prev_l - chars[c][0]), steps[1] + abs(prev_r - chars[c][0])) + dist
        go_right = min(steps[0] + abs(prev_l - chars[c][1]), steps[1] + abs(prev_r - chars[c][1])) + dist
        # 도착지는 반대방향
        prev_l, prev_r = chars[c][1], chars[c][0]
        steps[0], steps[1] = go_left, go_right

    print(min(steps))

if __name__ == "__main__":
    solution()
