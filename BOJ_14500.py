n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

num_list = set()

# oooo
for i in range(n):
    for j in range(m-3):
        num_list.add(sum(matrix[i][j:j+4]))

# o
# o
# o
# o

for i in range(n-3):
    for j in range(m):
        num_list.add(matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j])

# oo
# oo

for i in range(n-1):
    for j in range(m-1):
        num_list.add(matrix[i][j] + matrix[i+1][j] + matrix[i][j+1] + matrix[i+1][j+1])
        
# ooo
# ooo


for i in range(n-1):
    for j in range(m-2):
        num_list.add(matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j])
        num_list.add(matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1])
        num_list.add(matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+2])
        
        num_list.add(matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i][j])
        num_list.add(matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i][j+1])
        num_list.add(matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i][j+2])
        
        num_list.add(matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j+2])
        num_list.add(matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1])
        
# oo
# oo
# oo

for i in range(n-2):
    for j in range(m-1):
        num_list.add(matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i][j+1])
        num_list.add(matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+1][j+1])
        num_list.add(matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1])
        
        num_list.add(matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i][j])
        num_list.add(matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i+1][j])
        num_list.add(matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i+2][j])
        
        num_list.add(matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1])
        num_list.add(matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j] + matrix[i+2][j])


print(max(num_list))