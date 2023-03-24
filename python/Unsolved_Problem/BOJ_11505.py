import sys
import math
input = sys.stdin.readline

MOD = 1_000_000_007

n_number, n_change, n_cal = map(int, input().split())

nums = [0] + [int(input()) for _ in range(n_number)]

tree = [0] * (1 << (math.ceil(math.log2(n_number)))+1)
command = [list(map(int, input().split())) for _ in range(n_change + n_cal)]

def init(start, end, node, left, right):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    mid = (start + end) // 2

    tree[node] = (init(start, mid, node*2, left, right) * init(mid+1, end, node*2+1, left, right)) % MOD
    return tree[node]

def multiply(start, end, node, left, right):
    if left <= start and end <= right:
        return tree[node]

    if end < left or right < start:
        return 1

    mid = (start + end) // 2

    return (multiply(start, mid, node*2, left, right) * multiply(mid+1, end, node*2+1, left, right)) % MOD

def update(start, end, node, index, diff):
    if index < start or end < index:
        return
    tree[node] = (tree[node] * diff) % MOD

    if start == end:
        return

    mid = (start + end) // 2

    update(start, mid, node*2, index, diff)
    update(mid+1, end, node*2+1, index, diff)

init(1, n_number, 1, 1, n_number)

for a, b, c in command:
    if a == 1:
        nums[b] = c
        init(1, n_number, 1, 1, n_number)
    else:
        print(int(multiply(1, n_number, 1, b, c)))
    # print(tree)
