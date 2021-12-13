n, m = map(int, input().split())
length_list = list(map(int, input().split()))

first = max(length_list)
last = sum(length_list)

def can_make(list, length, m):
    norm = 0
    bluray_num = 1
    for num in list:
        if (norm + num) > length:
            bluray_num += 1
            norm = num
        else:
            norm += num
        if bluray_num > m:
            return False
    return True

while first < last:
    mid = (first + last) // 2
    if can_make(length_list, mid, m):
        last = mid
    else:
        first = mid + 1
        
print(first)