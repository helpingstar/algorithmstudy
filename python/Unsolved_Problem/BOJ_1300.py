n = int(input())
k = int(input())

def check_how_many(number, n):
    equal_count = 0
    under_number = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j < number:
                under_number += 1
            elif i * j == number:
                equal_count += 1
    return (under_number, equal_count)

first = 1
last = n * n

while first <= last:
    mid = (first + last) // 2
    if sum(check_how_many(mid, n)) < k:
        first = mid + 1
    elif check_how_many(mid, n)[0] <= k < sum(check_how_many(mid, n)):
        first = mid
        break
    else:
        last = mid - 1
        
print(first)