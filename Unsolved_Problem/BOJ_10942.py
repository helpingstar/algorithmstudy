n = int(input())

num_list = list(map(int, input().split()))

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    if num_list[a-1:b] == num_list[a-1:b][::-1]:
        print(1)
    else:
        print(0)