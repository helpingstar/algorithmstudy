target = int(input())
ans = abs(100 - target)
M = int(input())


# speed
# list : iterate
# set  : check wheter it contain x, add x, remove x
# https://stackoverflow.com/q/32917388/13114854
# https://stackoverflow.com/q/8929284/13114854

if M:
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001): 
    for N in str(num):
        if N in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)