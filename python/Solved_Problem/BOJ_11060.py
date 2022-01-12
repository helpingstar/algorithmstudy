n = int(input())
jump_list = list(map(int, input().split()))

min_jump_list = [n] * n

min_jump_list[0] = 0

for i in range(n):
    for j in range(1, jump_list[i]+1):
        if i + j >= n:
            continue
        min_jump_list[i + j] = min((min_jump_list[i+j], min_jump_list[i] + 1))
        
if min_jump_list[n-1] == n:
    print(-1)
else:
    print(min_jump_list[n-1])