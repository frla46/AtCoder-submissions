m = int(input())
d = [int(i) for i in input().split()]
t = (sum(d) + 1) // 2
su = 0
for i in range(m):
    su += d[i]
    if su >= t:
        print(i + 1, t - (su - d[i]))
        exit()
