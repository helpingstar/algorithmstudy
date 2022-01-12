n1, n2 = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

num_matrix = []
for _ in range(n1 + 1):
    num_matrix.append([0] * (n2+1))



for i in range(n1):
    for j in range(n2):
        if list1[i] == list2[j]:
            max_list = []
            for k in range(i + 1):
                max_list.append(max(num_matrix[k][:j+1]))
            num_matrix[i+1][j+1] = max(max_list) + 1

max = max(max(num_matrix))

num_list = []
norm_num = n2
for i in range(max, 0, -1):
    for j in range(n1, 0, -1):
        if i in num_matrix[j]:
            