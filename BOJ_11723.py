import sys

m = int(sys.stdin.readline().rstrip())
num_set = set()

for _ in range(m):
    operation = sys.stdin.readline().rstrip()
    
    if operation == 'all':
        num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif operation == 'empty':
        num_set = set()
    else:
        func, num = operation.split()
        num = int(num)
        if func == 'add':
            if num in num_set:
                continue
            num_set.add(num)
        elif func == 'remove':
            if num not in num_set:
                continue
            num_set.remove(num)
        elif func == 'check':
            if num in num_set:
                print(1)
            else:
                print(0)
        elif func == 'toggle':
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)