import bisect

n = int(input())

num_list = list(map(int, input().split()))

arr = []

for num in num_list:
    pos = bisect.bisect_left(arr, num)
    if len(arr) == pos:
        arr.append(num)
    else:
        arr[pos] = num

print(len(arr))
