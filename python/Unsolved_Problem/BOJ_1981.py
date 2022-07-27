# 배열에서의 이동
import sys
input= sys.stdin.readline
from collections import deque
N=int(input().rstrip())
dx=[0,1,0,-1]
dy=[1,0,-1,0]
board=[]
numLst=set()
for i in range(N):
    tmp=list(map(int,input().split()))
    for value in tmp:
        numLst.add(value)
    board.append(tmp)
# 정렬된 numLST에 투포인터라는 개념을 이용한다.
numLst=sorted(list(numLst))
visited=[[0 for _ in range(N)]for _ in range(N)]
visited_cnt=0

def solve():
    low,high=0,0
    ans=sys.maxsize
    while low<len(numLst) and high<len(numLst):
        # bfs로 탐색햇을 때, 중간지점들이 내가 정한 최소/최대 값 범위에 있는지 확인 
        if bfs(numLst[low],numLst[high]):
            if low==high:
                print(0)
                return
            #무사히 n-1,n-1에 도달했다면, 내가 정한 최소/최대값의 범위를 줄인다. 
            else:
                ans=min(ans,abs(numLst[high]-numLst[low]))
                low +=1
        #만약 도달하지 못했다면, 최댓값을 늘려서, 탐색범위를 늘려본다.
        else:
            high+=1
    print(ans)

def bfs(low,high):
    global visited,visited_cnt
    if board[0][0] < low or board[0][0] > high:
        return False
    visited_cnt+=1
    visited[0][0] =visited_cnt
    dq=deque([(0,0)])
    while dq:
        y,x=dq.popleft()
        if y==N-1 and x==N-1:
            return True
        for k in range(4):
            ny=y+dy[k]
            nx=x+dx[k]
            if not (0<=ny<N and 0<=nx<N):
                continue
            if visited[ny][nx] !=visited_cnt and low<=board[ny][nx]<=high:
                dq.append((ny,nx))
                visited[ny][nx] = visited_cnt
    return False

solve()