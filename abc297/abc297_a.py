n, d = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
for t1, t2 in zip(t, t[1:]):
    if t2 - t1 <= d:
        print(t2)
        break
else:
    print(-1)
