n = int(input())

def is_prime(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def dfs(num, cnt):
    if cnt == n:
        if is_prime(num):
            print(num)
    
    if not is_prime(num):
        return
    
    for i in range(1, 10):
        dfs(num * 10 + i, cnt + 1)
    

for i in range(2, 10):
    dfs(i, 1)