n = int(input())

cal_list = [n] * (n + 1)

cal_list[1] = 0

for i in range(1, n):
    if i <= (n // 3):
        if cal_list[i*3] > (cal_list[i] + 1):
            cal_list[i*3] = cal_list[i] + 1 
        if cal_list[i*2] > (cal_list[i] + 1):
            cal_list[i*2] = cal_list[i] + 1
        if cal_list[i+1] > cal_list[i] + 1:
            cal_list[i+1] = cal_list[i] + 1
    elif (n // 3) < i <= (n // 2):
        if cal_list[i*2] > (cal_list[i] + 1):
            cal_list[i*2] = cal_list[i] + 1
        if cal_list[i+1] > cal_list[i] + 1:
            cal_list[i+1] = cal_list[i] + 1
    else:
        if cal_list[i+1] > cal_list[i] + 1:
            cal_list[i+1] = cal_list[i] + 1
            
print(cal_list[n])