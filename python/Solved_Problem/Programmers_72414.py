def str_to_sec(string):
    hour = int(string[:2])
    min = int(string[3:5])
    sec = int(string[-2:])

    return ((hour * 60) + min) * 60 + sec

def sec_to_str(time):
    sec = time % 60
    time //= 60
    min = time % 60
    time //= 60
    hour = time

    return f'{hour:02d}:{min:02d}:{sec:02d}'

def solution(play_time, adv_time, logs):
    END = str_to_sec(play_time)
    adv_interval = str_to_sec(adv_time)
    played = [0] * (END + 1)
    for log in logs:
        start = str_to_sec(log[:8])
        end = str_to_sec(log[-8:])

        played[start] += 1
        played[end] -= 1
    for i in range(END+1):
        played[i] += played[i-1]

    start_point = 0
    sum_people = 0
    for i in range(adv_interval):
        sum_people += played[i]

    max_people = sum_people

    for i in range(1, END - adv_interval+1):
        sum_people -= played[i-1]
        sum_people += played[i + adv_interval-1]

        if sum_people > max_people:
            max_people = sum_people
            start_point = i

    answer = sec_to_str(start_point)
    return answer
