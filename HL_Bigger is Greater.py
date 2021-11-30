
def biggerIsGreater(w):
    w_num = len(w)
    chars = list(w)
    # 1글자일 경우 경우가 없기 때문에 무조건 no answer
    if w_num == 1:
        return 'no answer'
    
    # 내림차순 정렬과 같으면 no answer 출력해도 되지만 그럼 시간 복잡도가 증가한다.
    # 최고수, 즉 내림차순 정렬의 경우 앞의 수가 뒷 수보다 무조건 크므로 뒷 수가 더 크면
    # False를 해서 no answer가 아니라는 것을 나타낸다
    no_ans = True
    for i in range(w_num-1):
        if chars[i] < chars[i+1]:
            no_ans = False
    if no_ans:
        return 'no answer'
    
    # 여기부터는 최고수가 아니다, 2글장일경우 그냥 바로 뒤집는다.
    if w_num == 2:
        return w[::-1]
    
    # 뒤에서부터 훑어서 i 인덱스 값 뒤의 값 중에서 i보다 큰 수중 가장 작은수를 찾아낸다.
    # 빨리 만족하는 i가 발견될 수록 i가 더 작은 자리 숫자라는 뜻이므로 즉시 바꿔야한다는 뜻이다.
    # 그 수와 i를 바꾸고 i 뒤를 오름차순 정렬하고 합치면 된다.
    change_str = []
    for i in range(w_num-1, 0, -1):
        for chr in chars[i:]:
            if chars[i-1] < chr:
                change_str.append(chr)
        if change_str:
            # 문자가 여러개일 경우 앞의 문자의 idx 가 min_idx로 될 수 있음
            min_idx = chars[i:].index(min(change_str)) + i
            chars[i-1], chars[min_idx] = chars[min_idx], chars[i-1]
            chars = chars[:i] + sorted(chars[i:])
            return ''.join(chars)
        

T = int(input().strip())

for _ in range(T):
    
    w = input()
    
    result = biggerIsGreater(w)
    print(result)