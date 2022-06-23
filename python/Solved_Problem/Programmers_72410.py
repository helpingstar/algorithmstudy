def solution(new_id):
    # 소문자화
    answer = ''
    cur = 0
    new_id = new_id.lower()
    for i in range(len(new_id)):
        if new_id[i] not in '~!@#$%^&*()=+[{]}:?,<>/':
            answer += new_id[i]
            
    answer3 = ''
    cur = 0
    while cur < len(answer):
        if answer[cur] == '.':
            n_cur = cur
            while n_cur < len(answer) and answer[n_cur] == '.':
                n_cur += 1
            if answer3:
                answer3 += '.'
            cur = n_cur
            continue
        answer3 += answer[cur]
        cur += 1
    
    if not answer3:
        answer3 = 'a'
    
    if len(answer3) >= 16:
        answer3 = answer3[:15]
    if answer3[-1] == '.':
        answer3 = answer3[:-1]
    
    if len(answer3) <= 2:
        temp = len(answer3)
        for i in range(3 - temp):
            answer3 += answer3[-1]
    return answer3