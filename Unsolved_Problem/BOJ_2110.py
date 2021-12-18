n, c = map(int, input().split())
house_list = []
diff_list = []
for _ in range(n):
    house_list.append(int(input()))

house_list.sort()

for i in range(n-1):
    diff_list.append(house_list[i+1] - house_list[i])
    
max = (house_list[-1] - house_list[0]) // (c-1)

def can_set(norm):
    difference = 0
    count = 0
    for diff in diff_list:
        difference += diff
        if difference >= norm:
            count += 1
            difference = 0
        if count >= (c - 1):
            return True
    return False

first = 1
last = max

while first < last:
    mid = (first + last) // 2
    if can_set(mid):
        first = mid
    else:
        last = mid - 1

print(first)