import sys

input = sys.stdin.readline

n = int(input())

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, paths):
        curr_node = self.head
        for file in paths.split('\\'):
            if file not in curr_node.children:
                curr_node.children[file] = Node(file)
            curr_node = curr_node.children[file]

    def print_all(self):
        self.dfs(self.head, 0)

    def dfs(self, node:Node, depth):
        if node.children:
            for child in sorted(node.children):
                print(' '*depth + node.children[child].key)
                self.dfs(node.children[child], depth+1)

trie = Trie()

for _ in range(n):
    path = input().rstrip()
    trie.insert(path)

trie.print_all()
