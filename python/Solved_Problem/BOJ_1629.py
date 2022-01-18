a, b, c = map(int, input().split())

bstr = []
while b > 0:
    bstr.append(b % 2)
    b //= 2

high_list = [a % c]

for i in range(len(bstr)):
    high_list.append((high_list[i]**2) % c)

result = 1
for i in range(len(bstr)):
    if bstr[i]:
        result *= high_list[i]
        result %= c

print(result)