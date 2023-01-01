from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n_doc, rank = map(int, input().split())
    docs = list(map(int, input().split()))

    doc_dic = dict()
    q = deque()
    for i, doc in enumerate(docs):
        if doc not in doc_dic:
            doc_dic[doc] = 0
        doc_dic[doc] += 1
        q.append((doc, i))

    cnt = 0
    while q:
        if q[0][0] == max(doc_dic.keys()):
            cnt += 1
            a, b = q.popleft()
            if doc_dic[a] == 1:
                del doc_dic[a]
            else:
                doc_dic[a] -= 1
            if b == rank:
                print(cnt)
                break
        else:
            q.append(q.popleft())
