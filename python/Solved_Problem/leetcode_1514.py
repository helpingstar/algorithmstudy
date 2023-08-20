from typing import List
from collections import deque

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        prob = [0] * n
        prob[start_node] = 1
        q = deque()
        q.append(start_node)
        while q:
            now = q.popleft()
            for nxt, dist in graph[now]:
                cost = prob[now] * dist
                if cost > prob[nxt]:
                    q.append(nxt)
                    prob[nxt] = cost

        return prob[end_node]
