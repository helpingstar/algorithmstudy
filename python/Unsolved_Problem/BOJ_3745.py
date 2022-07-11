import sys
input = sys.stdin.readline
import bisect

INF = 100001

while True:
    try:
        max_n = 1
        cnt = 1
        n = int(input())
        table = [INF] * n
        stocks = list(map(int, input().split()))
        for i in range(n):
            table_idx = bisect.bisect_left(table, stocks[i])
            if stocks[i] < table[table_idx]:
                table[table_idx] = stocks[i]
        print(bisect.bisect_left(table, INF))
    except:
        break