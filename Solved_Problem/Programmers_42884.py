routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    while routes:
        num = routes[0][1]
        new_routes = []
        for i in routes:
            if i[0] > num:
                new_routes.append(i)
        routes = new_routes
        answer += 1
    return answer

print(solution(routes))