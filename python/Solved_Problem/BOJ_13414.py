import sys

input = sys.stdin.readline

limit, click = map(int, input().split())
q = []
check = set()

studs = [input().rstrip() for _ in range(click)]

studs = reversed(studs)

new_studs = []

for stud in studs:
    if stud in check:
        continue

    check.add(stud)
    new_studs.append(stud)
print(*reversed(new_studs[-limit:]), sep='\n')
