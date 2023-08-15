from collections import deque
s = deque(input())
q = int(input())
cnt = 0
for _ in range(q):
    l = input().split()
    if int(l[0]) == 1:
        cnt += 1
    else:
        if (cnt + int(l[1])) % 2 == 0:
            s.append(l[2])
        else:
            s.appendleft(l[2])
s = ''.join(s)
print(s if cnt % 2 == 0 else s[::-1])
