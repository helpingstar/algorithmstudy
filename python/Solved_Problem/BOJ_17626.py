n = int(input())
distance = [5] * (n+1)

square_max = int(n ** 0.5)
square_list = []
for i in range(1, square_max +1):
    square_list.append(i*i)
    distance[i*i] = 1

for i in range(1, n+1):
    for square in square_list:
        if i + (square) > n or distance[i] == 4:
            break
        if distance[i + square] > distance[i] + 1:
            distance[i + square] = distance[i] + 1

print(distance[n])
