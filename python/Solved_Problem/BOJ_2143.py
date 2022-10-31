import sys

input = sys.stdin.readline

target = int(input())
n_a = int(input())
a_list = list(map(int, input().split()))
n_b = int(input())
b_list = list(map(int, input().split()))

a_temp = []
a_sum = []
temp = 0

for a in a_list:
    temp += a
    a_sum.append(temp)
    a_temp.append(temp)
    
for i in range(n_a-1):
    for j in range(i+1, n_a):
        a_sum.append(a_temp[j] - a_temp[i])

b_temp = []
b_sum = []
temp = 0

for b in b_list:
    temp += b
    b_sum.append(temp)
    b_temp.append(temp)

for i in range(n_b-1):
    for j in range(i+1, n_b):
        b_sum.append(b_temp[j] - b_temp[i])

a_sum.sort()
b_sum.sort()

a_cur, b_cur = 0, len(b_sum)-1

ans = 0

# print(f'debug  {a_sum}')
# print(f"debug  {b_sum}")

while a_cur < len(a_sum) and 0 <= b_cur:
    # print(f'[debug] a_cur : {a_cur}, b_cur : {b_cur}')
    if a_sum[a_cur] + b_sum[b_cur] < target:
        a_cur += 1
    elif a_sum[a_cur] + b_sum[b_cur] > target:
        b_cur -= 1
    else:
        a_next = a_cur + 1
        while a_next < len(a_sum) and a_sum[a_cur] == a_sum[a_next]:
            a_next += 1
        b_next = b_cur - 1
        while b_next >= 0 and b_sum[b_cur] == b_sum[b_next]:
            b_next -= 1
        # print(f'[debug]        {a_next} - {a_cur}  |  {b_cur} - {b_next}')
        ans += (a_next - a_cur) * (b_cur - b_next)
        a_cur = a_next
        b_cur = b_next
print(ans)