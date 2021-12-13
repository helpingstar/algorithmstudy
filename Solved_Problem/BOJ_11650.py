import sys

n = int(sys.stdin.readline())
num_list = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    num_list.append((a, b))
    
num_list.sort()

for num in num_list:
    print(num[0], num[1])