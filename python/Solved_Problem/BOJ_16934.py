import sys

input = sys.stdin.readline

class Node:
    def __init__(self, key, data=0) -> None:
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        already_print = False
        for idx, char in enumerate(string):
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
                if not already_print:
                    print(string[:idx+1])
                    already_print = True
            curr_node = curr_node.children[char]
        if curr_node.data == 0:
            curr_node.data = 1
            if not already_print:
                print(string)
        else:
            curr_node.data += 1
            print(string+str(curr_node.data))

n = int(input())
trie = Trie()
for _ in range(n):
    temp = input().rstrip()
    trie.insert(temp)
