import sys

num_list = [0] * 10001

n = int(sys.stdin.readline())

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i]:
        for _ in range(num_list[i]):
            print(i)