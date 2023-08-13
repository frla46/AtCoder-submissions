from collections import deque
n, c, k = [int(i) for i in input().split()]
t = deque(sorted([int(input()) for _ in range(n)]))
cnt = 0
while len(t) > 0:
    cnt += 1
    t1 = t[0]
    hc = 1
    while len(t) > 0 and t1 + k >= t[0] and hc <= c:
        t.popleft()
        hc += 1
print(cnt)
