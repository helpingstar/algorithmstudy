n, r, c = map(int, input().split())
result = 0
while 0 < n:
    r_quo, c_quo  = r // (2 ** (n-1)), c // (2 ** (n-1))
    
    if r_quo == 0:
        if c_quo == 0:
            pass
        else:
            result += 2 ** (2 * (n-1))
            c -= 2 ** (n - 1)
    else:
        if c_quo == 0:
            result += 2 ** (2 * (n-1)) * 2
            r -= 2 ** (n - 1)
        else:
            result += 2 ** (2 * (n - 1)) * 3
            r -= 2 ** (n - 1)
            c -= 2 ** (n - 1)
    n -= 1
    
print(result)