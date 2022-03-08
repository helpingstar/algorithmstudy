import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

jews = []
bags = []

for _ in range(n):
    m, v = map(int, input().split())
    jews.append((m, v))

for _ in range(k):
    c = int(input())
    bags.append(c)

jews.sort()
bags.sort()

max = -1
result = 0

q = []

j_ptr = 0

for bag in bags:
    # 첫 번째 조건 : j_ptr 이 jews의 index를 초과하지 않기 위함
    # 두 번째 조건 : 보석이 가방의 무게 이하인지 확인하기 위함
    while j_ptr < len(jews) and jews[j_ptr][0] <= bag:
        heapq.heappush(q, -jews[j_ptr][1])
        j_ptr += 1
    if q:
        # 큰 순서대로 이미 쌓아놨기 때문에 1 bag 당 1 pop이 가능하다
        # 앞에서 넣은 것은 무조건 지금의 bag보다 무게가 작기 때문에
        # 앞의 내용을 다시 탐색할 필요가 없고 그 때문에 O(n) 이 가능하다.
        result += -heapq.heappop(q)

print(result)