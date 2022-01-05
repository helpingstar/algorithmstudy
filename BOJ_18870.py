import sys

n = int(sys.stdin.readline().rstrip())

num_list = list(map(int, sys.stdin.readline().split()))

num_dic = {}

for i in num_list:
    if i in num_dic.keys():
        num_dic[i] += 1
    else:
        num_dic[i] = 1

total = 0
t = list(num_dic.items())
print(t)
t.sort()
print(t)

for i in t:
    total += i[1]
    num_dic[i[0]] = total

print(num_dic)