n = int(input())
s = sorted([int(input()) for _ in range(n)])
t = sum(s)
for i in s:
    if t % 10 != 0:
        print(t)
        exit()
    elif i % 10 != 0:
        t -= i
print(0)

