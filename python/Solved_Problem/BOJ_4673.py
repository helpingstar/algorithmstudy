check = set()

for i in range(1, 10000):
    check.add(i + sum(map(int, list(str(i)))))

for i in range(1, 10000):
    if i in check:
        continue
    print(i)
