import sys

input = sys.stdin.readline

n, q = map(int, input().split())

first = [0] + list(map(int, input().split()))
tree = [0] * (n * 4)
    
def init(start, end, node):
    if start == end:
        tree[node] = first[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid+1, end, node * 2 + 1)
    return tree[node]

def sum(start, end, node, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2+1, left, right)

def add_diff(start, end, node, index, diff):
    if index < start or end < index:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    add_diff(start, mid, node*2, index, diff)
    add_diff(mid+1, end, node*2+1, index, diff)
    
init(1, n, 1)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    x, y = min(x, y), max(x, y)
    print(sum(1, n, 1, x, y))
    add_diff(1, n, 1, a, b - first[a])
    first[a] = b