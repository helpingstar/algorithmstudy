import sys

n = sys.stdin.readline().rstrip()
n_len = len(n)
n = int(n)


m = int(sys.stdin.readline().rstrip())

broken_num_list = list(map(int, sys.stdin.readline().split()))

unbroken_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
zero_is_broken = False

for broken_num in unbroken_num_list:
    if broken_num == 0:
        zero_is_broken = True
        continue
    unbroken_num_list.remove(broken_num)

nominee_list = []

lowest_nominee = int('1' * (n_len - 1)) * unbroken_num_list[-1]
if zero_is_broken:
    highest_nominee = int('1' * (n_len + 1)) * unbroken_num_list[0]
else:
    highest_nominee = unbroken_num_list[0] * (10 ** n_len)
    
nominee_list.append(lowest_nominee)
nominee_list.append(highest_nominee)

