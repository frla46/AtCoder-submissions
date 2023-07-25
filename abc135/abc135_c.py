n = int(input())
a = [int(i) for i in input().split()]
enemy = sum(a)
b = [int(i) for i in input().split()]
cnt = 0
for i in range(n):
    a[i + 1] = max(0, min(a[i] + a[i + 1] - b[i], a[i + 1]))
    a[i] = max(0, a[i] - b[i])
defeat = sum(a)
print(enemy - defeat)
