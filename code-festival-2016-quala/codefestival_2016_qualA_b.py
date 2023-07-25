n = int(input())
a = [int(i) for i in input().split()]
cnt = 0
for i in range(n):
    j = a[i]
    if a[j - 1] == i + 1:
        cnt += 1
print(cnt // 2)
