# 유니온으로 풀자!
import sys

input=sys.stdin.readline

n,m,k=map(int,input().split())
power=list(map(int,input().split()))

def find_parent(parent,x):
    if parent[x] !=x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

parent=[0]*(n+1)
arr=[]

for i in range(1,n+1):
    # 발전소라면 parent가 0이다
    if i in power:
        continue
    # 발전소가 아니라면 자기자신
    parent[i]=i

for i in range(m):
    s,e,d=map(int,input().split())
    arr.append((s,e,d))

result=0

arr.sort(key=lambda x:x[2])

for ele in arr:
    s,e,d=ele
    if find_parent(parent,s)!=find_parent(parent,e):
        union_parent(parent,s,e)
        result+=d

print(result)