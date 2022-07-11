"""
우측부분을 이진탐색으로 찾고 -1부분을 인덱스 지정한다
그리고 낮은 것부터 왼쪽으로 가면서 하나씩 load한다.
한 iter마다 sort 해서 작은것부터 할 수 있게 한다.
"""


import sys
import bisect
import heapq
input = sys.stdin.readline


def solution():
    n_crane = int(input())
    w_crane = list(map(int, input().split()))

    n_box = int(input())
    w_box = list(map(int, input().split()))

    w_crane.sort()
    w_box.sort()

    if w_crane[-1] < w_box[-1]:
        return -1

    box_visited = [False] * n_box
    p_crane = []

    for crane in w_crane:
        right = bisect.bisect_right(w_box, crane)
        p_crane.append(right-1)
        
    iter = 0
    cnt = 0
    while cnt < n_box:
        for i in range(n_crane):
            ptr = p_crane[i]
            
            if ptr < 0:
                continue

            while box_visited[ptr] == True:
                ptr -= 1
                if ptr < 0:
                    break

            if ptr < 0:
                continue

            box_visited[ptr] = True
            ptr-=1
            cnt += 1
            p_crane[i] = ptr
        iter += 1
        p_crane.sort()

    return iter



print(solution())