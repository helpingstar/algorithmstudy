n = int(input())

dict = {i : [] for i in range(201)}

for _ in range(n):
    age, name = input().split()
    age = int(age)
    dict[age].append(name)

for i in range(201):
    if dict[i]:
        for name in dict[i]:
            print(i, name)
            