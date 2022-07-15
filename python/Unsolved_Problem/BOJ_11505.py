import sys
import math
input = sys.stdin.readline

n, m, k = map(int, input().split())

first = [0]
tree = [0] * (n * 4)

for _ in range(n):
    first.append(int(input()))
    
def init(start, end, node):
    if start == end:
        tree[node] = first[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = (init(start, mid, node * 2) * init(mid+1, end, node * 2 + 1)) % 1000000007
    return tree[node]

def dup(start, end, node, left, right):
    if end < left or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return (dup(start, mid, node*2, left, right) * dup(mid+1, end, node*2+1, left, right)) % 1000000007

def dup_diff(start, end, node, index, diff):
    if index < start or end < index:
        return
    tree[node] *= diff
    tree[node] %= 1000000007
    if start == end:
        return
    mid = (start + end) // 2
    dup_diff(start, mid, node*2, index, diff)
    dup_diff(mid+1, end, node*2+1, index, diff)
    
init(1, n, 1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        if first[b] == 0:
            first[b] = c
            init(1, n, 1)
        else:
            dup_diff(1, n, 1, b, c / first[b])
        first[b] = c
    else:
        print(int(dup(1, n, 1, b, c)))