import copy

def lilysHomework(arr):
    asc_count = 0
    des_count = 0
    length = len(arr)
    des_arr = copy.deepcopy(arr)
    for i in range(length - 1):
        min_idx = i
        for j in range(i+1, length):
            if arr[min_idx] > arr[j]:
                min_idx = j
        if i != min_idx:
            asc_count += 1
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
    for i in range(length - 1):
        max_idx = i
        for j in range(i+1, length):
            if des_arr[max_idx] < des_arr[j]:
                max_idx = j
        if i != max_idx:
            des_count += 1
            des_arr[max_idx], des_arr[i] = des_arr[i], des_arr[max_idx]
            
    return min((asc_count, des_count))
                
            
    
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
print(lilysHomework(arr))