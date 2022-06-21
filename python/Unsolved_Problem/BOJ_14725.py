import sys


input = sys.stdin.readline

n = int(input())

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
        for word in string.split():
            if word not in curr_node.children:
                curr_node.children[word] = Node(word)
            curr_node = curr_node.children[word]
    
def tree_print(root:Node, cnt):
    for child in sorted(root.children.values(), key=lambda x: x.key):
        print('-'*(cnt*2) + child.key, sep='')
        if child.children:
            tree_print(child, cnt+1)

trie = Trie()
for _ in range(n):
    trie.insert(input().rstrip()[2:])

tree_print(trie.head, 0)