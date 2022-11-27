n=int(input())

chess_map=[]
black=[]
white=[]
color=[[0]*n for _ in range(n)]

for i in range(n):
    chess_map.append(list(map(int, input().split())))
    for j in range(n):
        # True가 검은색
        if chess_map[i][j]==1 and (i + j) % 2 == 0:
            black.append((i,j))
            color[i][j] = 1
        # False가 흰색
        if chess_map[i][j]==1 and (i + j) % 2 == 1:
            white.append((i,j))
            color[i][j] = 0

# 검은색인 경우
Bcnt=0
# 흰색인 경우
Wcnt=0

isused01=[0]*(n*2-1)
isused02=[0]*(n*2-1)

def fun(bishop,index,count):
    global Bcnt, Wcnt
    if index==len(bishop):
        rx,ry=bishop[index-1]
        # 블랙이면 Bcnt 최대값
        if color[rx][ry]:
            Bcnt=max(Bcnt,count)
        # 흰색이면 Wcnt 최대값
        else:
            Wcnt=max(Wcnt,count)
        return

    x,y=bishop[index]
    if isused01[x+y] or isused02[x-y+n-1]:
        fun(bishop,index+1,count)
    else:
        isused01[x+y]=1
        isused02[x-y+n-1]=1
        fun(bishop,index+1,count+1)
        isused01[x+y]=0
        isused02[x-y+n-1]=0
        fun(bishop,index+1,count)

if len(black)>0:
    fun(black,0,0)
if len(white)>0:
    fun(white,0,0)
print(Bcnt+Wcnt)
