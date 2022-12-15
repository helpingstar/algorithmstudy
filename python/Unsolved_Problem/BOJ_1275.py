import sys

input = sys.stdin.readline

n, q = map(int, input().split())

nums = [0] + list(map(int, input().split()))

tree = [0] * (n * 4)

def assign_tree(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = start + (end - start) // 2
    tree[node] = assign_tree(start, mid, node*2) + assign_tree(mid+1, end, node*2+1)
    return tree[node]

def get_sum(start, end, node, left, right):
    # print(f'[debug]  {start, end, node, left, right}')
    if left <= start and end <= right:
        return tree[node]
    if end < left or right < start:
        return 0
    mid = start + (end - start) // 2
    return get_sum(start, mid, node*2, left, right) + \
        get_sum(mid+1, end, node*2+1, left, right)

def update_diff(start, end, node, diff, index):
    # print(f'[debug]  {start, end, node, diff, index}')
    if index < start or end < index:
        return
    tree[node] += diff
    if start == end:
        return
    mid = start + (end-start) // 2
    update_diff(start, mid, node*2, diff, index)
    update_diff(mid+1, end, node*2+1, diff, index)

assign_tree(1, n, 1)

# print(tree)

for _ in range(q):
    a, b, c, d = map(int, input().split())
    a, b = min(a, b), max(a, b)
    print(get_sum(1, n, 1, a, b))
    update_diff(1, n, 1, d - nums[c], c)
    nums[c] = d
