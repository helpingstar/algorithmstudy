import sys
import math

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())

    tree = [0] * (1 << (math.ceil(math.log2(65536)) + 1))
    nums = [int(input()) for _ in range(N)]

    def update(start, end, index, node, diff):
        if index < start or end < index:
            return
        tree[node] += diff
        if start == end:
            return
        mid = (start + end) // 2
        update(start, mid, index, node*2, diff)
        update(mid+1, end, index, node*2 + 1, diff)

    def find(start, end, node, k):
        if start == end:
            return start
        mid = (start + end) // 2
        if tree[node*2] >= k:
            return find(start, mid, node*2, k)
        else:
            return find(mid+1, end, node*2+1, k - tree[node*2])

    result = 0
    for i in range(K-1):
        update(0, 65535, nums[i], 1, 1)

    for i in range(K-1, N):
        update(0, 65535, nums[i], 1, 1)
        result += find(0, 65535, 1, (K+1)//2)
        update(0, 65535, nums[i-K+1], 1, -1)

    print(result)


solution()
