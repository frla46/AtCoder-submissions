n = int(input())
li = [[int(i) for i in input().split()] for _ in range(n)]
sum = 0
for i in range(n):
    for j in range(n):
        sum += ((li[i][0] - li[j][0]) ** 2 + (li[i][1] - li[j][1]) ** 2) ** 0.5
print(sum / n)
