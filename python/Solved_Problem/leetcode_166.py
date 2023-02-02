def solution():
    numerator, denominator = map(int ,input().split())

    is_minus = False
    if numerator * denominator < 0:
        is_minus = True
    n, d = abs(numerator), abs(denominator)
    check = dict()
    mok = n // d
    result = f'{mok}'
    if mok > 0:
        n %= (mok*d)
    n *= 10
    if n == 0:
        return result
    result += '.'
    while n != 0 and len(result) < 10 ** 4:
        if n not in check:
            check[n] = len(result)
        else:
            result = f'{result[:check[n]]}({result[check[n]:len(result)]})'
            break
        mok = n // d
        if mok > 0:
            n %= (mok*d)
        result += str(mok)
        n *= 10
    if is_minus:
        return '-' + result
    else:
        return result
    
print(solution())