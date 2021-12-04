n = int(input())

quo = n // 5
remain = n % 5

if quo:
    if remain == 2:
        if quo == 1:
            print(-1)
        else:
            print(quo+2)
    elif remain in [1, 3]:
        print(quo + 1)
    elif remain == 4:
        print(quo + 2)
    else:
        print(quo)
else:
    if remain == 3:
        print(1)
    else:
        print(-1)