from collections import deque, defaultdict
from typing import *

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length = len(beginWord)
        word_dict = defaultdict(set)
        if endWord not in wordList:
            return 0
        for word in wordList:
            for i in range(length):
                word_dict[word[:i] + '-' + word[i+1:]].add(word)

        # print(f'[debug]  word_dict: {word_dict}')

        q = deque()
        q.append((beginWord, {beginWord}))
        while q:
            now_word, visited = q.popleft()
            # print(f'[debug]  {now_word}, {dist}, {visited}')
            for i in range(length):
                for next_word in word_dict[now_word[:i]+'-'+now_word[i+1:]]:
                    # print(f'[debug]  next_word: {next_word}')
                    if next_word in visited:
                        continue
                    if next_word == endWord:
                        # print(f'[return] now: {now_word} next: {next_word}, visited: {visited}')
                        return len(visited)+1
                    if next_word not in visited:
                        q.append((next_word, visited | {next_word}))
        return 0
