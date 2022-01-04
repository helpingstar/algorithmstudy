import sys

n, m = map(int, sys.stdin.readline().split())
pok_2_num = {}
num_2_pok = {}

for i in range(n):
    pok = sys.stdin.readline().rstrip()
    pok_2_num[pok] = i
    num_2_pok[i] = pok
    
for _ in range(m):
    what = sys.stdin.readline().rstrip()
    if what.isdigit():
        print(num_2_pok[int(what) - 1])
    else:
        print(pok_2_num[what] + 1)