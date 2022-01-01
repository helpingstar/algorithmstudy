n, k = map(int, input().split())


if k < n:
    print(n-k)
else:
    n_list = [100001] * (2*k)
    
    for i in range(1, n+1):
        n_list[i] = n-i
    for i in range(1, n):
        if n_list[i] + 1 < n_list[2 * i]:
            n_list[2*i] = n_list[i] + 1
    for i in range(n, 2*k):
        p = i
        while n_list[p-1] > n_list[p] + 1:
            n_list[p-1] = n_list[p] + 1
            if n_list[(p-1) * 2] > n_list[p-1] + 1:
                n_list[(p-1) * 2] = n_list[p-1] + 1
            p -= 1
        if n_list[i+1] > n_list[i] + 1:
            n_list[i+1] = n_list[i] + 1
        if i < k:
            if n_list[2*i] > n_list[i] + 1:
                n_list[2*i] = n_list[i] + 1
    print(n_list[k])