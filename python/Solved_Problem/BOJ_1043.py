import sys
from tabnanny import check
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

# 진실을 아는 사람 초기값 초기화, 0일때는 안함
trueman_number = input()
if trueman_number != 0:
    first_know_man = list(map(int, trueman_number.split()[1:]))
    
# 진실을 아는 사람 테이블
know_true_check = [False] * (n+1)
for i in first_know_man:
    know_true_check[i] = True

# 파티 참석자들을 기록함, 그래프를 만듬
party_table = []
graph = [set() for _ in range(n+1)]
for _ in range(m):
    guys = list(map(int, input().split()[1:]))
    for i in guys:
        graph[i] |= set(guys)
    party_table.append(guys)

# bfs 수행
q = deque(first_know_man)
while q:
    t = q.popleft()
    for man in graph[t]:
        if know_true_check[man]:
            continue
        q.append(man)
        know_true_check[man] = True

# True가 있는지 체크하는 함수
def check_true(one_party):
    for i in one_party:
        if know_true_check[i]:
            return 0
    return 1

result = 0
for one_party in party_table:
    result += check_true(one_party)
        
print(result)