from collections import deque, defaultdict
from typing import *
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dic = defaultdict(set)
        word_length = defaultdict(int)

        for word in wordDict:
            word_dic[word[0]].add(word)
            word_length[word[0]] = max(word_length[word[0]], len(word))

        visited = set()
        visited.add(0)
        q = deque()
        q.append(0)
        while q:
            now = q.popleft()
            if s[now] not in word_dic:
                continue
            for i in range(now+1, min(now + word_length[s[now]]+1, len(s)+1)):
                if s[now:i] in word_dic[s[now]]:
                    if i == len(s):
                        return True
                    if i not in visited:
                        visited.add(i)
                        q.append(i)
        return False
