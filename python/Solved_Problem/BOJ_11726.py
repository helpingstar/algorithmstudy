n = int(input())

num_list = [0] * (n+1)

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    num_list[1], num_list[2] = 1, 2
    for i in range(3, n+1):
        num_list[i] = num_list[i-1] + num_list[i-2]
    print(num_list[n] % 10007)

