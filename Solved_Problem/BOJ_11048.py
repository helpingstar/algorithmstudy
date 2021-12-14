n, m = map(int, input().split())
candy_matrix = []

for _ in range(n):
    candy_matrix.append(list(map(int, input().split())))

get_candy_matrix = []
for _ in range(n):
    get_candy_matrix.append([0] * m)

if n == 1 and m ==1:
    print(candy_matrix[0][0])
elif n == 1 and m != 1:
    total = 0
    for i in range(m):
        total += candy_matrix[0][i]
    print(total)
elif m == 1 and n != 1:
    total = 0
    for i in range(n):
        total += candy_matrix[i][0]
    print(total)
else:
    get_candy_matrix[0][0] = candy_matrix[0][0]
    get_candy_matrix[0][1] = candy_matrix[0][0] + candy_matrix[0][1]
    get_candy_matrix[1][0] = candy_matrix[0][0] + candy_matrix[1][0] 

    for col in range(2, m):
        get_candy_matrix[0][col] = get_candy_matrix[0][col - 1] + candy_matrix[0][col]
        
    for row in range(2, n):
        get_candy_matrix[row][0] = get_candy_matrix[row - 1][0] + candy_matrix[row][0]

    for row in range(1, n):
        for col in range(1, m):
            get_candy_matrix[row][col] = max((get_candy_matrix[row-1][col-1], get_candy_matrix[row-1][col], get_candy_matrix[row][col-1])) + candy_matrix[row][col]


    print(get_candy_matrix[n-1][m-1])
