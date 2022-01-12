import sys

n, m = map(int, sys.stdin.readline().split())

site_dict = {}

for _ in range(n):
    site, pwd = sys.stdin.readline().split()
    site_dict[site] = pwd

for _ in range(m):
    input_site = sys.stdin.readline().rstrip()
    print(site_dict[input_site])