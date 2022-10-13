target = int(input())
n = int(input())
sum = 0
for _ in range(n):
    a, b = map(int, input().split())
    sum += a * b

if sum == target:
    print("Yes")
else:
    print("No")
