import sys
import heapq    

input = sys.stdin.readline

n_jewel, n_bag = map(int, input().split())

jewel_list = [list(map(int, input().split())) for _ in range(n_jewel)]
bag_list = [int(input()) for _ in range(n_bag)]

jewel_list.sort(key=lambda x: -x[0])
bag_list.sort()

q = []
result = 0

for bag in bag_list:
    while jewel_list and jewel_list[-1][0] <= bag:
        mass, value = jewel_list.pop()
        heapq.heappush(q, -value)
    
    if q:
        result += -heapq.heappop(q)
        
print(result)