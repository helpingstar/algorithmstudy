import sys

input = sys.stdin.readline

t = int(input())

def solution():
    length = int(input())
    preorder = [0] + list(map(int, input().split()))
    inorder = [0] + list(map(int, input().split()))

    inorder_index_map = [0] * (length+1)
    for i, num in enumerate(inorder):
        inorder_index_map[num] = i

    preorder_index = 0
    # print(f'[debug] {inorder_index_map}')
    def postorder(start, end, left, right):
        nonlocal preorder_index
        # print(f'[debug]  {(start, end, left, right)}')
        if start > end:
            return
        preorder_index += 1
        root_value = preorder[preorder_index]
        root_index = inorder_index_map[root_value]
        postorder(start, root_index-1, left, right)
        postorder(root_index+1, end, left, right)
        print(root_value, end=' ')

    postorder(1, length, 1, length)
    print()

for _ in range(t):
    solution()
