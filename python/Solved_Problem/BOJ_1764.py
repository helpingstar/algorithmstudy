import sys



n, m = map(int, sys.stdin.readline().rstrip().split())

a_set = set()
b_set = set()

for _ in range(n):
    a_set.add(sys.stdin.readline().rstrip())

for _ in range(m):
    b_set.add(sys.stdin.readline().rstrip())
    
db_list = list(a_set & b_set)
db_list.sort()

print(len(db_list))
for name in db_list:
    print(name)
