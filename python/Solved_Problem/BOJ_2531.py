import sys

input = sys.stdin.readline

n_dish, n_sushi, n_continue, coupon = map(int, input().split())

belt = [int(input()) for _ in range(n_dish)]

eat = [0] * (n_sushi + 1)
count = 0
ans = 0
for i in range(n_continue):
    if not eat[belt[i]]:
        count += 1
    eat[belt[i]] += 1

ans = count
if not eat[coupon]:
    ans += 1

tail = 0
head = n_continue - 1
# print(f'[debug]  eat: {eat}')
for i in range(n_dish):
    head += 1
    new_head = head % n_dish

    if not eat[belt[new_head]]:
        count += 1
    eat[belt[new_head]] += 1
    new_tail = tail % n_dish
    if eat[belt[new_tail]] == 1:
        count -= 1
    eat[belt[new_tail]] -= 1
    tail += 1

    if eat[coupon]:
        bonus = 0
    else:
        bonus = 1
    # print(f'[debug]  eat: {eat}')
    ans = max(ans, count + bonus)

print(ans)
