import sys
import heapq

n = int(sys.stdin.readline().rstrip())

num_list = []

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    
    if num == 0:
        if num_list:
            print(heapq.heappop(num_list))
        else:
            print(0)
    else:
        heapq.heappush(num_list, num)