"""
Trie 자료구조를 몰라서 개념을 배우고 풀었다.
"""

import sys

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.number = 0

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        curved = False
        nickname = ''
        for char in string:
            # 문제 조건이 트리 조건상 꺾으면 그 인덱스 까지가 nickname이다
            if not curved:
                nickname += char

            if char not in curr_node.children:
                # 꺾으면 꺾인 문자까지 반영하고(위에서) 그 이후는 닉네임 반영할 필요가 없다.
                if not curved:
                    curved = True
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        
        # 중복으로 할 필요가 없으므로 똑같은 정보가 들어오면 number를 증가시킨다.
        curr_node.number += 1
        if not curr_node.data:
            curr_node.data = string
        
        # 꺾은 경험이 있다면 저장된 nickname을 출력한다.
        if curved:
            print(nickname)
        # 꺾은 적이 없다 = 있는 것의 진부분집합 or 같다.
        else:
            # abcd 후에 ab를 추가하면 ab1이 되는 현상이 있어서 추가된 조건(진부분집합)
            if curr_node.number == 1:
                print(string)
            # 기존에 있던 data일 경우
            else:
                print(string + str(curr_node.number))

input = sys.stdin.readline

n = int(input())
trie = Trie()
for _ in range(n):
    trie.insert(input().rstrip())