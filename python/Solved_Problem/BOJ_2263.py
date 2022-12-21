import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_index_map = [0] * (n+1)
for i, num in enumerate(inorder):
    inorder_index_map[num] = i

def dp(in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right:
        return
    # print(f'[debug]  {(in_left, in_right, post_left, post_right)}')
    root = postorder[post_right]
    root_index = inorder_index_map[root]
    n_left = root_index - in_left
    n_right = in_right - root_index

    print(root, end=' ')
    dp(in_left, in_left + n_left - 1, post_left, post_left + n_left -1)
    dp(in_right - n_right + 1, in_right, post_right-n_right, post_right - 1)

dp(0, n-1, 0, n-1)
