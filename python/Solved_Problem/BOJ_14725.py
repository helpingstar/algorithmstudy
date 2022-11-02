import sys

input = sys.stdin.readline

from typing import List

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, words):
        curr_node = self.head
        for word in words.split():
            if word not in curr_node.children:
                curr_node.children[word] = Node(word)
            curr_node = curr_node.children[word]
    def print_all(self):
        self.print_dfs(self.head, 0)
    def print_dfs(self, node:Node, depth:int):
        for child in sorted(node.children):
            print(f"{'--'*depth}{node.children[child].key}")
            self.print_dfs(node.children[child], depth+1)

n = int(input())
trie = Trie()
for _ in range(n):
    sen = input().rstrip()
    trie.insert(sen[2:])

trie.print_all()
