n = int(input())
a1 = [int(i) for i in input().split()]
a2 = [int(i) for i in input().split()]
max = 0
for i in range(n):
    cnt = sum(a1[:i + 1] + a2[i:])
    if max < cnt:
        max = cnt
print(max)
