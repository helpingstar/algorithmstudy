import sys

input = sys.stdin.readline

INF = int(1e9)

n, q = map(int, input().split())

nums = [0] + [int(input()) for _ in range(n)]
tree = [[0, 0] for _ in range(n*4)]

# min, max
def init(left, right, node):
    if left == right:
        tree[node] = [nums[left], nums[left]]
        return tree[node]
    mid = left + (right - left) // 2
    l_min, l_max = init(left, mid, node*2)
    r_min, r_max = init(mid+1, right, node*2+1)
    tree[node][0] = min(l_min, r_min)
    tree[node][1] = max(l_max, r_max)
    return tree[node]

def get_min_max(start, end, node, left, right):
    # print(f'[debug]  {start, end, node, left, right}')
    if right < start or end < left:
        return [INF, 0]
    if left <= start and end <= right:
        return tree[node]
    mid = start + (end - start) // 2
    l_min, l_max = get_min_max(start, mid, node*2, left, right)
    r_min, r_max = get_min_max(mid+1, end, node*2+1, left, right)
    return min(l_min, r_min), max(l_max, r_max)

init(1, n, 1)
for _ in range(q):
    a, b = map(int, input().split())
    print(*get_min_max(1, n, 1, a, b))
