from collections import defaultdict

def solution(gems):
    if not gems:
        return False
    gem_list = set(gems)

    length = len(gems)
    gem_kind_num = len(gem_list)
    l = r = 0
    my_gem_dic = defaultdict(int)
    my_gem_set = set()
    my_gem_dic[gems[0]] += 1
    my_gem_set.add(gems[0])

    ans_length = length + 1
    ans_l, ans_r = length + 1, length + 1

    while l <= r < length:
        if len(my_gem_set) == gem_kind_num:
            if r-l < ans_length:
                ans_length = r-l
                ans_l, ans_r = l, r
            my_gem_dic[gems[l]] -= 1
            if my_gem_dic[gems[l]] == 0:
                my_gem_set.remove(gems[l])
            l += 1
        else:
            if r < length - 1:
                # print(f'[debug] r : {r}')
                my_gem_dic[gems[r+1]] += 1
                if my_gem_dic[gems[r+1]] == 1:
                    my_gem_set.add(gems[r+1])
            r += 1

    return [ans_l+1, ans_r+1]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
