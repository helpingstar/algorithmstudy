import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
time_list = defaultdict(list)

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    time_list[b].append(a)

last_finished = 0
count = 0
count_not_same = 0
count_same = 0
for item in sorted(time_list.items()):
    for start_time in item[1]:
        if last_finished <= start_time < item[0]:
            count_not_same += 1
        elif start_time == item[0]:
            count_same += 1
    if count_same or count_not_same:
        last_finished = item[0]
        if count_not_same and count_same:
            count += (count_same + 1)
        elif count_not_same == 0:
            count += (count_same)
        else:
            count += 1
    count_not_same = 0
    count_same = 0
        
print(count)