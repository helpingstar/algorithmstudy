import sys
import math

MOD = 1000000007

input = sys.stdin.readline

N, M, K = map(int, input().split())

nums = [0] + [int(input()) for _ in range(N)]

tree = [0] * (1 << (math.ceil(math.log2(N)) + 1))

def init(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) * init(mid+1, end, node*2+1) % MOD
    return tree[node]

def multiply(start, end, node, left, right):
    if end < left or right < start:
        return 1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    return multiply(start, mid, node*2, left, right) * multiply(mid+1, end, node*2+1, left, right) % MOD

def update(start, end, node, index, n_new):
    if not (start <= index <= end):
        return

    if start == end:
        tree[node] = n_new
        return


    mid = (start + end) // 2
    update(start, mid, node*2, index, n_new)
    update(mid+1, end, node*2+1, index, n_new)
    tree[node] = tree[node*2] * tree[node*2 + 1] % MOD

init(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, N, 1, b, c)
    else:
        print(multiply(1, N, 1, b, c))
        # print(tree)
