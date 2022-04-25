import sys
from collections import defaultdict

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n_folder, n_file = map(int, input().split())
main = defaultdict(list)

for _ in range(n_folder + n_file):
    parent, child, isfolder = input().rstrip().split()
    main[parent].append((child, isfolder))

q = int(input())

file_set = set()

def get_files(folder_name):
    cnt = 0
    for child, isfolder in main[folder_name]:
        if isfolder == '1':
            cnt += get_files(child)
        else:
            file_set.add(child)
            cnt += 1
    return cnt

for _ in range(q):
    sequence = input().split('/')
    num = get_files(sequence[-1].rstrip())
    print(len(file_set), num)
    file_set = set()