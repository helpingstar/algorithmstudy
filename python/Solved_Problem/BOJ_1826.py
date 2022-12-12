import sys
import heapq
input = sys.stdin.readline

def solution():
    n = int(input())
    station_list = []
    for _ in range(n):
        station_list.append(list(map(int, input().split())))

    dest, init_fuel = map(int, input().split())
    station_list.sort()
    fuel = init_fuel
    pos = 0
    ans = 0
    station_cur = 0
    q = []
    while True:
        pos += fuel
        # print(f'[debug]  fuel: {fuel}, pos: {pos}')
        fuel = 0
        if pos >= dest:
            return ans
        while station_cur < n and station_list[station_cur][0] <= pos:
            heapq.heappush(q, -station_list[station_cur][1])
            station_cur += 1
        # print(f'[debug]  q: {q}')
        if not q:
            return -1
        else:
            ans += 1
            fuel += -heapq.heappop(q)

print(solution())
