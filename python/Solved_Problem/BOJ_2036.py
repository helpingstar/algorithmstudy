n = int(input())
plus = []
minus = []
zero = 0
one = 0
score = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    elif num == 1:
        one += 1
    else:
        zero += 1
        
plus.sort()
minus.sort()

if len(plus) > 1:
    if len(plus) % 2:
        score += plus[0]
        plus = plus[1:]
    for i in range(0, len(plus), 2):
        score += (plus[i] * plus[i+1])
elif len(plus) == 1:
    score += plus[0]

score += one

if zero:
    if len(minus) == 1:
        pass
    else:
        if len(minus) % 2:
            minus = minus[0:-1]
        for i in range(0, len(minus), 2):
            score += (minus[i] * minus[i+1])
else:
    if len(minus) == 1:
        score += minus[0]
    else:
        if len(minus) % 2:
            score += minus[-1]
            minus = minus[0:-1]
        for i in range(0, len(minus), 2):
            score += (minus[i] * minus[i+1])
            
print(score)