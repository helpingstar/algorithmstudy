import sys
from collections import deque

input = sys.stdin.readline

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, path):
        curr_node = self.head
        for file in path:
            if file not in curr_node.children:
                curr_node.children[file] = Node(file)
            curr_node = curr_node.children[file]

    def search(self, path):
        curr_node = self.head
        for file in path:
            if file in curr_node.children:
                curr_node = curr_node.children[file]
            else:
                return False
        if curr_node.data != None:
            return True


def dfs_node(node:Node, depth:int):
    print(' '*depth, node.key, sep='')
    for child in sorted(node.children):
        dfs_node(node.children[child], depth+1)



path_list = []
n = int(input())
trie = Trie()
for _ in range(n):
    trie.insert(input().rstrip().split('\\'))

for node in sorted(trie.head.children):
    dfs_node(trie.head.children[node], 0)
