from collections import deque

n, k = map(int, input().split())

sec_list = [100001] * 100001

sec_list[n] = 0

def get_fastest_time(n, k):
    if k <= n:
        return (n - k, 1)
    else:
        time = 100001
        count = 0
        queue = deque()
        queue.append(n)
        while queue:
            t = queue.popleft()
            if sec_list[t] >= time:
                return (time, count)
            for i in [t, -1, 1]:
                if not 0 <= t + i <= 100000:
                    continue
                if sec_list[t + i] < sec_list[t] + 1:
                    continue
                queue.append(t+i)
                sec_list[t+i] = sec_list[t] + 1
                if t + i == k:
                    time = sec_list[t+i]
                    count += 1

print(*get_fastest_time(n, k), sep='\n')