import heapq

def solution(people, limit):
    people.sort(reverse=True)
    q = []
    heapq.heappush(q, 0)
    answer = 0
    for num in people:
        if num <= -q[0]:
            temp = heapq.heappop(q)
            temp += num
        else:
            answer += 1
            heapq.heappush(q, -limit + num)

    return answer

people = [98, 99]
limit = 100
print(solution(people, limit))
