n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    n_list = [0] * (n+1)
    n_list[1], n_list[2] = 1, 3

    for i in range(3, n+1):
        n_list[i] = n_list[i-1] + (2 * n_list[i-2])

    print(n_list[n] % 10007)