import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    k, m, p = map(int, input().split())
    degree = [0] * (m+1)
    order = [0] * (m+1)
    # 자기"가" 가리키는 node
    graph = [[] for _ in range(m+1)]
    # 자기"를" 가리키는 node
    node_num = [[] for _ in range(m+1)]

    for _ in range(p):
        # a -> b
        a, b = map(int ,input().split())
        # a"가" 가리키는 b
        graph[a].append(b)
        # b"를" 가리키는 a
        node_num[b].append(a)

        degree[b] += 1

    q = deque()
    for i in range(1, m+1):
        if degree[i] == 0:
            # 첫 order, q에 append 하고 order 는 1로 한다.
            q.append(i)
            order[i] = 1

    while q:
        now = q.popleft()
        for i in graph[now]:
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)
                # 최고값 구하고 개수 세기
                # max_order : 최고 order
                max_order = -1
                # max_cnt : max_order이 있는 개수
                max_cnt = 0
                for j in node_num[i]:
                    # max_order보다 크면 갱신하고 cnt = 1
                    if max_order < order[j]:
                        max_order = order[j]
                        max_cnt = 1
                    # max_order과 같으면 cnt += 1
                    elif max_order == order[j]:
                        max_cnt += 1
                if max_cnt == 1:
                    order[i] = max_order
                else:
                    order[i] = max_order + 1

    print(k ,max(order))