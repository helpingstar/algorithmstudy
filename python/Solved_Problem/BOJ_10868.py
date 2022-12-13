import sys

input = sys.stdin.readline
INF = sys.maxsize
n_num, n_question = map(int, input().split())

nums = [0] + [int(input()) for _ in range(n_num)]
tree = [0] * (n_num * 4)

def assign_tree(left, right, node):

    if left > right:
        return INF

    if left == right:
        tree[node] = nums[left]
        return tree[node]


    mid = (left + right) // 2

    tree[node] = min(assign_tree(left, mid, node*2), assign_tree(mid+1, right, node*2+1))
    return tree[node]

def get_min(start, end, node, left, right):
    # print(f'[debug]  {start, end, node, left, right}')
    if end < left or right < start:
        return INF
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2

    return min(get_min(start, mid, node*2, left, right), get_min(mid+1, end, node*2+1, left, right))

assign_tree(1, n_num, 1)
# print(tree)
for _ in range(n_question):
    a, b = map(int, input().split())
    print(get_min(1, n_num, 1, a, b))
