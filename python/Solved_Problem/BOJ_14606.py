n = int(input())

def dp(num):
    if num == 1:
        return 0
    
    temp = num // 2
    return temp * (num - temp) + dp(temp) + dp(num-temp)

print(dp(n))