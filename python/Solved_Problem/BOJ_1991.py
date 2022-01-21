import sys
from collections import defaultdict
input = sys.stdin.readline

graph = defaultdict(lambda: [None, None])

n = int(input())
for _ in range(n):
    n, l, r = input().split()
    graph[n][0] = l
    graph[n][1] = r
    
def preorder(root):
    if root == '.' or not root:
        return
    print(root, end='')
    preorder(graph[root][0])
    preorder(graph[root][1])
    
def inorder(root):
    if root == '.' or not root:
        return
    inorder(graph[root][0])
    print(root, end='')
    inorder(graph[root][1])
    
def postorder(root):
    if root == '.' or not root:
        return
    postorder(graph[root][0])
    postorder(graph[root][1])
    print(root, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')