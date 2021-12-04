num, gate_num = map(int, input().split())
line = list(map(int, input().split()))

gate = list(0 for _ in range(gate_num))

success = True

for i in line:
    temp = [g for g in gate if g < i]
    if not temp:
        success = False
        break
    max_temp = max(temp)
    gate[gate.index(max_temp)] = i

if success:
    print('YES')
else:
    print('NO')