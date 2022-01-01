nums = input()
total = 0
number = ''
minus_flag = False
cal = ''
for n in nums:
    if n.isdigit():
        number += n
    else:
        if cal == '':
            total += int(number)
        elif cal == '-':
            total -= int(number)
            minus_flag = True
            
        elif cal == '+':
            if minus_flag:
                total -= int(number)
            else:
                total += int(number)
        cal = n
        number = ''

if cal == '':
    total += int(number)
elif cal == '-':
    total -= int(number)
    minus_flag = True
    
elif cal == '+':
    if minus_flag:
        total -= int(number)
    else:
        total += int(number)
print(total)