import heapq

def exist_two(food_list, K):
    if food_list[0] > K and food_list[1] > K:
        return 0
    elif (food_list[0] < K < food_list[1]) or (food_list[1] < K < food_list[0]):
        return 1
    else:
        min_num = min(food_list)
        max_num = max(food_list)
        if min_num + (max_num * 2) > K:
            return 1
        else:
            return -1


def solution(scoville, K):
    if len(scoville) == 2:
        return exist_two(scoville, K)

    lower_than_k = []
    upper_than_k = []
    for food in scoville:
        if food < K:
            heapq.heappush(lower_than_k, food)
        else:
            heapq.heappush(upper_than_k, food)

    if len(lower_than_k) == 0:
        return 0
    elif len(lower_than_k) == 1:
        return 1
    else:
        count = 0
        while lower_than_k:
            n1 = heapq.heappop(lower_than_k)
            n2 = heapq.heappop(lower_than_k)
            result = n1 + (n2 * 2)
            if result > K:
                heapq.heappush(upper_than_k, result)
                count += 1
            else:
                heapq.heappush(lower_than_k, result)
                count += 1
            if len(lower_than_k) == 1:
                if upper_than_k:
                    return count + 1
                else:
                    return -1
        return count