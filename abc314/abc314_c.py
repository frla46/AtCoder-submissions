from collections import deque
n, m = [int(i) for i in input().split()]
s = input()
c = [int(i) for i in input().split()]
ret = ''
li = [deque() for _ in range(m)]
for n, i in enumerate(c):
    li[i - 1].append(s[n])
for i in li:
    i.appendleft(i.pop())
for i in c:
    ret += li[i - 1].popleft()
print(ret)
