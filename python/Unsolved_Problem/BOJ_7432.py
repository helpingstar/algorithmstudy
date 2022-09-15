import sys
from collections import OrderedDict

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

def print_all(head:Node, count):
    print(' '*count + head.key)
    for child_node in sorted(head.children.keys()):
        print_all(head.children[child_node], count+1)

n = int(input())
trie = Trie()
for _ in range(n):
    trie.insert(input().split('\\'))

for child_node in sorted(trie.head.children.keys()):
    print_all(trie.head.children[child_node], 0)
