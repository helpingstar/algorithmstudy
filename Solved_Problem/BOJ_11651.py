import sys

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    num_list.append((a, b))
    
num_list.sort(key=lambda x: (x[1], x[0]))

for i in num_list:
    print(i[0], i[1])
    