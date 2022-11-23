n_array = int(input())
num_list = list(map(int, input().split()))

lp1 = [0] * n_array
lp2 = [0] * n_array

for i in range(n_array):
    lc = rc = i
    while lc >= 0 and rc < n_array and num_list[lc] == num_list[rc]:
        lc -= 1
        rc += 1
    lp1[i] = (rc-lc) // 2

for i in range(n_array-1):
    lc, rc = i, i+1
    if num_list[lc] == num_list[rc]:
        while lc >= 0 and rc < n_array and num_list[lc] == num_list[rc]:
            lc -= 1
            rc += 1
        lp2[i] = (rc-lc) // 2
    else:
        lp2[i] = 0

n_question = int(input())

for _ in range(n_question):
    a, b = map(int, input().split())
    center = (b - a) // 2 - 1
    if (b - a) % 2 == 0:
        result = (b - a) // 2 >= lp1[center]
    else:
        result = (b - a) // 2 >= lp2[center]

    if result:
        print(1)
    else:
        print(0)
