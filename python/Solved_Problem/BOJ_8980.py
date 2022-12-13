import sys

input = sys.stdin.readline

n_city, capacity = map(int, input().split())

n_box = int(input())

box_list = []
box_burden = [0] * (n_city+1)
for _ in range(n_box):
    a, b, c = map(int, input().split())
    box_list.append((a, b ,c))

box_list.sort(key=lambda x: x[1])
result = 0
for a, b, c in box_list:
    temp = min(c, capacity - max(box_burden[a:b]))
    for i in range(a, b):
        box_burden[i] += temp
    result += temp
    # print(f'[debug]  temp: {temp}')

print(result)
