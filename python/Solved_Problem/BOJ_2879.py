import sys

input = sys.stdin.readline

def cal_tab(in_list):
    if len(in_list) == 0:
        return 0
    elif len(in_list) == 1:
        return in_list[0]
    else:
        result = 0
        min_value = min(in_list)
        min_index = in_list.index(min_value)
        result += min_value
        result += max(0, cal_tab(in_list[:min_index]) - min_value)
        result += max(0, cal_tab(in_list[min_index+1:]) - min_value)
        return result

def solution():
    ans = 0
    n = int(input())
    cur_tab = list(map(int, input().split()))
    tar_tab = list(map(int ,input().split()))

    diff_tab = [cur_tab[i] - tar_tab[i] for i in range(n)]

    is_plus = True
    tmp = []
    for num in diff_tab:
        if num > 0:
            if is_plus:
                tmp.append(abs(num))
            else:
                ans += cal_tab(tmp)
                tmp = [abs(num)]
                is_plus = not is_plus
        else:
            if not is_plus:
                tmp.append(abs(num))
            else:
                ans += cal_tab(tmp)
                tmp = [abs(num)]
                is_plus = not is_plus

    ans += cal_tab(tmp)
    print(ans)

solution()
