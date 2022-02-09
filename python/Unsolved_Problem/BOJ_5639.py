import sys

prefix = [1, 2, 3]
stack = []
postfix = []
count = 0

# for i in range(10000):
#     try:
#         n = int(sys.stdin.readline().strip())
#         prefix.append(n)

#     except:
#         break
    
for i in prefix:
    if len(stack) < 2:
        stack.append(i)
    elif stack[-1] < i and stack[-2] < i:
        while len(stack) >= 2 and stack[-1] < i and stack[-2] < i:
            postfix.append(stack.pop())
        if len(stack) < 2:
            stack.append(i)
        else:
            postfix.append(i)
    else:
        stack.append(i)
while stack:
    postfix.append(stack.pop())

print(*postfix, sep='\n')