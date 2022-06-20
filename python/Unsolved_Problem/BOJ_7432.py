import sys
input = sys.stdin.readline
from collections import OrderedDict

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    def insert(self, string):
        curr_node = self.head
        for char in string.split("\\"):
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
    
n = int(input())
trie = Trie()

for _ in range(n):
    trie.insert(input().rstrip())

def dfs(root: Node, cnt: int):
    if root.children:
        for child_node in sorted(root.children.values(), key=lambda x: x.key):
            print(' '*cnt, child_node.key, sep='')
            dfs(child_node, cnt+1)

dfs(trie.head, 0)