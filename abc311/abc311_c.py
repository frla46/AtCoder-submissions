n = int(input())
a = [0] + [int(i) for i in input().split()]
i = 1
for _ in range(n):
    i = a[i]
s = [i]
while s[0] != a[i]:
    i = a[i]
    s.append(i)
print(len(s))
print(*s)


