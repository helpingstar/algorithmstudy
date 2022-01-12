people = [70, 80, 50]
limit = 100

# 처음에 2명 최대인거 몰라서 잘못품
# 2트에서 다풀고 시간초과남
# 3트에서 1번 시간초과

def solution(people, limit):  
    answer = 0
    people.sort()
    # while people:
    #     num = limit - people.pop()
    #     if people:
    #         if people[0] <= num:
    #             people.pop(0) 
    #     answer += 1
    
    left, right = 0, len(people) - 1
    while left <= right:
        if limit - people[right] >= people[left]:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    
    return answer

print(solution(people, limit))
