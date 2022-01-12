n, k = map(int, input().split())
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

num_list = [10001] * (k+1)

for i in coin_list:
    if i <= k:
        num_list[i] = 1

for i in range(1, k+1):
    for coin in coin_list:
        if (i + coin) > k:
            continue
        if (num_list[i] + 1) < num_list[i + coin]:
            num_list[i + coin] = num_list[i] + 1

if num_list[k] == 10001:
    print(-1)
else:
    print(num_list[k])