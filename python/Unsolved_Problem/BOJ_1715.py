import sys
import heapq

input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
    s = int(input())
    heapq.heappush(q, s)

result = 0

# N개의 숫자를 넣으면 누적 더하기 연산은 N-1을 해야 한다는 것을 생각하면 풀리는 문제
# 더한 것은 계속 더해지므로 작은것 부터 하는 것이 좋기 때문에 heapq를 사용한다.
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    temp = a+b
    result += temp
    heapq.heappush(q, temp)

print(result)
