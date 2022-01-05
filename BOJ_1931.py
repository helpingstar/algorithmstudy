import sys

n = int(sys.stdin.readline().rstrip())
time_list = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    time_list.append((a, b))
    


time_list.sort(key=lambda x: x[1])

def dy_list(time_list):
    if not time_list:
        return 1
    
    _, end = time_list.pop(0)
    new_list = []
    for time in time_list:
        if time[0] >= end:
            new_list.append(time)
    return 1 + dy_list(new_list)

print(dy_list(time_list) - 1)