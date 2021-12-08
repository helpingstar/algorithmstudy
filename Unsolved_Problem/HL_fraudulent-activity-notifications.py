def get_median(cnt_num, d):
    cnt = 0
    if d % 2:
        for i in range(len(cnt_num)):
            cnt += cnt_num[i]
            if cnt > d // 2:
                return i
    else:
        first = 0
        second = 0
        for i in range(len(cnt_num)):
            cnt += cnt_num[i]
            # if the number is even, the two numbers you have to deal with are d//2 and d//2 + 1 
            if cnt == (d // 2):
                first = i
            elif cnt > (d//2):
                if first:
                    second = i
                    return (first + second) / 2
                else:
                    first = i
                    second = i
                    return (first + second) / 2
                    

def activityNotifications(expenditure, d):
    cnt_num = [0] * 201
    notification = 0
    for i in range(d):
        cnt_num[expenditure[i]] += 1
    for i in range(d, n):
        if get_median(cnt_num, d) * 2 <= expenditure[i]:
            notification += 1
        cnt_num[expenditure[i]] += 1
        cnt_num[expenditure[i-d]] -= 1
    return notification
        


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
expenditure = list(map(int, input().rstrip().split()))
result = activityNotifications(expenditure, d)
print(result)