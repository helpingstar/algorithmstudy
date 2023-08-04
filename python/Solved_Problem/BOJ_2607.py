import sys
from collections import defaultdict
input = sys.stdin.readline


def solution():
    N = int(input())
    myword = input().rstrip()
    my_dic = defaultdict(int)
    for c in myword:
        my_dic[c] += 1

    def checker(vs_dic):
        nonlocal my_dic
        plus = minus = 0
        key_list = set(my_dic.keys())
        for k in vs_dic.keys():
            key_list.add(k)
        key_list = list(key_list)
        for c in key_list:
            if abs(vs_dic[c] - my_dic[c]) > 1:
                return False
            elif vs_dic[c] - my_dic[c] == 1:
                if plus == 1:
                    return False
                else:
                    plus = 1
            elif vs_dic[c] - my_dic[c] == -1:
                if minus == 1:
                    return False
                else:
                    minus = 1
        return True
    result = 0
    for _ in range(N-1):
        word = input().rstrip()
        w_dic = defaultdict(int)
        for c in word:
            w_dic[c] += 1
        if checker(w_dic):
            result += 1

    print(result)


solution()
