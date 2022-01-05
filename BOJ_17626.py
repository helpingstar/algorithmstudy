n = int(input())

square_max = int(n ** 0.5)

squares_list = [0] * (n+1)

enter = []
for i in range(1, square_max+1):
    squares_list[i] = 1
    