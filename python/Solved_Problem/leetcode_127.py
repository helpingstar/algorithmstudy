from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or endWord not in wordList:
            return 0
        length = len(beginWord)
        medium_to_word = defaultdict(list)
        for word in wordList:
            for i in range(length):
                medium = word[:i] + '-' + word[i+1:]
                medium_to_word[medium].append(word)

        visited = set()
        visited.add(beginWord)
        q = deque()
        q.append((beginWord, 0))
        while q:
            now, count = q.popleft()
            next_medium_list = []
            for i in range(length):
                medium = now[:i] + '-' + now[i+1:]
                next_medium_list.append(medium)
            # print(f'[debug]  next_medium: {next_medium_list}')
            for next_medium in next_medium_list:
                for next in medium_to_word[next_medium]:
                    # print(f'[debug]  next:{next}')
                    if next in visited:
                        continue
                    if next == endWord:
                        return count + 2
                    q.append((next, count+1))
                    visited.add(next)
        return 0
