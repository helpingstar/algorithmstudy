# **알고리즘 리뷰**

## **2021-12-02**

### **3. [Ema's Supercomputer](https://www.hackerrank.com/challenges/two-pluses/problem)**

#### **내 생각**
십자가를 찾고, 십자가가 유효한 자리인지 검증하는 것 까지는 했다

하지만 큰 수부터 탐색하기 때문에 

5 > 1 or 3 > 3 이렇게 발견될 수 있다

몇몇 문제는 해결되지만 곱하면 후자가 더 큰데 이것은 어떻게 해결해야 할 지 모르겠다. 기존 방식대로 하면 런타임이 기하급수적으로 늘어난다.

공부를 더 한다음에 다시 풀어봐야겠다.

## **2021-12-04**

### **1. [타겟 넘버](https://programmers.co.kr/learn/courses/30/lessons/43165)**
### **2. [섬 연결하기](https://programmers.co.kr/learn/courses/30/lessons/42861)**

## **2021-12-07**

### **1. [BOJ 17471](https://www.acmicpc.net/problem/17471)**

## **2021-12-08**

### **1. [HL_lilys-homework](https://www.hackerrank.com/challenges/lilys-homework/problem)**
### **시도**
시도 조건이 절댓값인지 모르고 오름차순으로 시도했으나 실패 -> 내림차순도 포함하여 시도했으나 몇개는 시간초과 몇개는 틀림 -> 앞에서 오름차순 연산 실행하고 정렬시켜버린것을 그대로 다시 내림차순 연산해서 `copy.deepcopy()`를 사용해서 고쳤으나 시간초과로 틀림 여기까지 선택정렬 사용함

### **2. [HL_fraudulent-activity-notifications](https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem)**
### **시도**
각 구역을 슬라이싱해서 소팅 후 `median`찾았으나 시간초과 

-> `queue`에 `popleft()`, `append()` 통해서 큐 구성 후 `median` 구하기 시간초과

-> `input()` -> `sys.stdin.readline()` 시간초과

-> `0 <= expenditure[i] <= 200` 이라는 힌트를 얻었다.

-> 답을 참고하여 어찌어찌 풀긴 했지만, 앞으로 `exceed time limit`, 취급해야 할 문자들의 범위가 좁다면 ex) `0 <= expenditure[i] <= 200` 계수 정렬을 활용해야겠다.

