n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

p_dict = {}

for i in range(1, n+1):
    p_dict[i] = []

for _ in range(m):
    parent, child = map(int, input().split())
    p_dict[parent].append(child)

