'''
backjoon url -> https://www.acmicpc.net/problem/16197

>> Keyword


>> P
N*M 크기 보드에 4개 버튼과 2개 동전으로 이루어진 게임
버튼은 상/하/좌/우 으로 구성, 두 동전이 동시에 이동
두 동전 중 하나만 떨어뜨리기 위한 최소 횟수 구하라
    - 칸은 빈칸과 벽으로 구성
    - 벽이면 동전 이동 안한다
    - 칸이 없으면 바깥으로 떨어진다.

>> S
아이디어
2차원 배열에서 동전을 하나만 떨어뜨려야해
동전 2개가 있고 문제의 범위가 크지 않으니(<=20) 2가지 경우 제외하고 큐에 담기를 반복하면?
    - 중복되는 경우(이동 후 두 동전이 같은 위치 존재)
    - 두 동전 모두 떨어지는 경우를 
++ 우선순위 큐를 사용하자 
어떻게?
큐에 담을 때 (이동횟수, x, y)로 담으면 이동횟수가 최소인 것부터 처리하니까!

접근
1. 라이브러리 추가 - heapq
2. 보드를 입력 받으며 두 동전 위치 따로 변수에 담기 - (x1, y1, x2, y2) -> param
3. 버튼 이동 리스트 추가 - move (-1,0) ...
4. 함수 호출
print(solve(x1, y1, x2, y2))
5. 함수 선언
def solve(x1, y1 ..) -> int:
    visit = set()
    q = []

    heapq.heappush((0, x1, y1, x2, y2))
    visit.add((x1, y1...))

    while q:
        cnt, x1, y1 = heapq.heappop(q)

        for dx, dy in move:
            nx1, ..
            nx2, ..

            if 하나만 떨어진경우:
                return cnt if cnt <= 10 else -1
            elif 둘다 보드 위에 존재할 경우:
                heapq.heappush(q, (cnt+1, ...))
    
'''






import heapq

def solve(coin1, coin2) -> int:
    visit = set()
    q = []

    heapq.heappush(q, (1, coin1[0], coin1[1], coin2[0], coin2[1]))
    visit.add((coin1[0], coin1[1], coin2[0], coin2[1]))

    while q:
        cnt, x1, y1, x2, y2 = heapq.heappop(q)

        for dx, dy in move:
            cx1, cy1 = x1+dx, y1+dy
            cx2, cy2 = x2+dx, y2+dy

            if (0 <= cx1 < N and 0 <= cy1 < M  \
                and not (0 <= cx2 < N and 0 <= cy2 < M)) \
                    or (0 <= cx2 < N and 0 <= cy2 < M \
                        and not (0 <= cx1 < N and 0 <= cy1 < M)):
                return cnt if cnt <= 10 else -1
            elif 0 <= cx1 < N and 0 <= cy1 < M and 0 <= cx2 < N and 0 <= cy2 < M:
                if board[cx1][cy1] == '#':
                    cx1, cy1 = x1, y1
                if board[cx2][cy2] == '#':
                    cx2, cy2 = x2, y2

                if ((cx1, cy1, cx2, cy2)) in visit:
                    continue

                heapq.heappush(q, (cnt+1, cx1, cy1, cx2, cy2))
                visit.add((cx1, cy1, cx2, cy2))

    return -1

N, M = map(int, input().split())
coin = []
board = []
for i in range(N):
    row = input()
    board.append(row)
    for j in range(M):
        if board[i][j] == 'o':
            coin.append((i, j))

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(solve(*coin))