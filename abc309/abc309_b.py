n = int(input())
l = []
for i in range(n):
    l += input().split()
for i in range(n):
    if i == 0:
        print(l[i + 1][0], l[i][:-1], sep='')
    elif i == n - 1:
        print(l[i][1:], l[i - 1][-1], sep='')
    else:
        print(l[i + 1][0], l[i][1:-1], l[i - 1][-1], sep='')
