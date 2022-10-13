vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

while True:
    answer = 0
    sen = input()
    if sen == '#':
        break
    for c in sen:
        if c in vowel:
            answer += 1
    print(answer)
