import sys

t = int(sys.stdin.readline().rstrip())

tri_list = [0] * 101
first = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(1, 11):
    tri_list[i] = first[i-1]
for i in range(11, 101):
    tri_list[i] = tri_list[i-1] + tri_list[i-5]

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(tri_list[n])