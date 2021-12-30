n, m = map(int, input().split())

pok_dict = {}
pok_list = []

for i in range(n):
    pok_name = input()
    pok_dict[pok_name] = i
    pok_list.append(pok_name)
for _ in range(m):
    problem = input()
    if problem.isdigit():
        print(pok_list[int(problem)-1])
    else:
        print(pok_dict[problem])