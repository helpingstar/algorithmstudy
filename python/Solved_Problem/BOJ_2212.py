"""
센서 위치를 오름차순으로 정렬하고 최대차를 구한다 (각 간격의 합)
그리고 나서 집중국 -1의 개수만큼 큰 순서대로 간격을 제거하면 된다
예를 들어 3 6 7 8 10 12 14 15 18 20 이면
차는       3 1 1 2  2  2  1  3  2
이다 여기서 센서를 묶는 다는 것은 간격 하나를 무기력하게 하는 효과가 있으므로
k-1의 개수만큼 없애면 된다.
"""

import sys
import heapq

input = sys.stdin.readline

def solution():

    n = int(input())
    k = int(input())
    road = list(map(int, input().split()))

    if n == 1:
        return 0

    road.sort()

    if k == 1:
        return road[-1] - road[0]

    diff = []
    sum = road[-1] - road[0]

    for i in range(n-1):
        heapq.heappush(diff, road[i]-road[i+1])
    
    for _ in range(k-1):
        sum += heapq.heappop(diff)

    return sum

print(solution())
