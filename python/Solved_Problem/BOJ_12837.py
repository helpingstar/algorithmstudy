import sys

input = sys.stdin.readline

n_day, q = map(int, input().split())

tree = [0] * (n_day * 4)

def get_sum(start, end, node, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return get_sum(start, mid, node*2, left, right) + get_sum(mid+1, end, node*2+1, left, right)

def update(start, end, node, diff, idx):
    if idx < start or end < idx:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node*2, diff, idx)
    update(mid+1, end, node*2+1, diff, idx)

for _ in range(q):
    query, a, b = map(int, input().split())

    if query == 1:
        update(1, n_day, 1, b, a)
    else:
        print(get_sum(1, n_day, 1, a, b))
