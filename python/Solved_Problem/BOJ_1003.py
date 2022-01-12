n = int(input())

n0_list = [0] * 41
n1_list = [0] * 41

n0_list[0] = 1
n1_list[1] = 1

for i in range(2, 41):
    n0_list[i] = n0_list[i-1] + n0_list[i-2]
    n1_list[i] = n1_list[i-1] + n1_list[i-2]

for _ in range(n):
    number = int(input())
    print(n0_list[number], n1_list[number])