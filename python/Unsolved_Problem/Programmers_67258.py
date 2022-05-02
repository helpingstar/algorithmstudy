from collections import defaultdict

def solution(gems):
    gem_kind = len(set(gems))
    gem_len = len(gems)
    answer = [0, gem_len-1]
    dic = defaultdict(int)
    dic[gems[0]] = 1
    l, r = 0, 0
    while l < gem_len and r < gem_len:
        if len(dic) < gem_kind:
            r += 1
            if r == gem_len:
                break
            dic[gems[r]] += 1
        else:
            if (r - l) < answer[1] - answer[0]:
                answer = [l, r]
            if dic[gems[l]] == 1:
                del dic[gems[l]]
            else:
                dic[gems[l]] -= 1
            l += 1
    
    answer[0] += 1
    answer[1] += 1
    return answer