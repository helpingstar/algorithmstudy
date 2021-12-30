n = int(input())
m = int(input())
string = input()

ioi = 'IO' * n + 'I'
count = 0

for i in range(m-(2*n + 1)):
    if string[i] == 'O':
        continue
    if string[i:i+(2*n + 1)] == ioi:
        count += 1
        
print(count)