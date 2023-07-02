import sys


def solve():
    input = sys.stdin.readline
    word = input().rstrip()
    bomb = input().rstrip()
    bomb_list = list(bomb)
    # 끝자리를 따로 저장하니까 속도 9% 감소
    checker = bomb[-1]
    q = []

    for c in word:
        q.append(c)
        if len(q) >= len(bomb) and c == checker:
            if q[-len(bomb):] == bomb_list:
                # for _ in range(len(bomb)):
                #     q.pop()
                # 14% 감소
                del q[-len(bomb):]

    if len(q) == 0:
        print("FRULA")
    else:
        print(''.join(q))


# 전역 프로그램에서 함수로 바꾸니까 50% 감소
if __name__ == "__main__":
    solve()
