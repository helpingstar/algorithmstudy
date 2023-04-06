import sys

max_b = '00000000'
min_b = '99999999'
min_name = ''
max_name = ''

for _ in range(int(input())):
    name, dd, mm, yyyy = input().split()
    dd, mm, yyyy = map(int, (dd, mm, yyyy))

    birth = f'{yyyy}{mm:02d}{dd:02d}'

    # print(f'[debug] (min_b, max_b, birth): {min_b, max_b, birth}')

    if min_b > birth:
        min_b = birth
        min_name = name
    if max_b < birth:
        max_b = birth
        max_name = name

print(max_name)
print(min_name)
