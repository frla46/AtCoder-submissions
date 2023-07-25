n = int(input())
v = [int(i) for i in input().split()]
v.sort()
t = (v[0] + v[1]) / 2
for i in range(n - 2):
    t = (t + v[i + 2]) / 2
print(t)
