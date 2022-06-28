import heapq

def dijkstra(n, start, graph):
    distance = [1e9] * (n+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return distance

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for start, end, cost in fares:
        graph[start].append((end, cost))
        graph[end].append((start, cost))
    
    s_ = dijkstra(n, s, graph)
    a_ = dijkstra(n, a, graph)
    b_ = dijkstra(n, b, graph)
    print(s_)
    answer = []
    
    answer.append(s_[a] + a_[b])
    answer.append(s_[b] + b_[a])
    answer.append(s_[a] + s_[b])
    
    for i in range(1, n+1):
        if i in [s, a, b]:
            continue
        answer.append(s_[i] + a_[i] + b_[i])
    
    return min(answer)