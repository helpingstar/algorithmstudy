def solution(arr):
    cnt = 0
    n = len(arr)
    sorted_arr = sorted(arr)
    index_dict = {arr[i] : i for i in range(n)}

    for i in range(n):
        if arr[i] != sorted_arr[i]:
            get_index = index_dict[sorted_arr[i]]
            index_dict[ arr[i] ] = index_dict[ sorted_arr[i]]
            arr[i], arr[get_index] = sorted_arr[i], arr[i]
            cnt += 1

    return cnt

def lilysHomework(arr):
    reversed_arr = list(reversed(arr))

    return min(solution(arr), solution(reversed_arr))
