word = input()
bomb = input()

stack = []

len_bomb = len(bomb)

for c in word:
    stack.append(c)
    if c == bomb[-1]:
        # To avoid out of index
        if len(stack) >= len_bomb:
            # check whether same or not
            if stack[-len_bomb:] == list(bomb):
                for _ in range(len_bomb):
                    stack.pop()

result = ''.join(stack)

if result:
    print(result)
else:
    print('FRULA')