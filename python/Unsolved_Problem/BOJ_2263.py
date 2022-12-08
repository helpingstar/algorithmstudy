import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_index_map = [0] * (n + 1)
for i in range(n):
    inorder_index_map[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return

    root = postorder[postEnd]

    n_left = inorder_index_map[root] - inStart
    n_right = inEnd - inorder_index_map[root]

    print(root, end = " ")
    preorder(inStart, inStart + n_left - 1, postStart, postStart + n_left - 1)
    preorder(inEnd - n_right + 1, inEnd, postEnd - n_right, postEnd - 1)

preorder(0, n - 1, 0, n - 1)
