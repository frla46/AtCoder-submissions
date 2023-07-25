A, B, M = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
x = [list(map(int, input().split())) for _ in range(M)]
min_ = min(a) + min(b)
for i in x:
    min_ = min(min_, a[i[0] - 1] + b[i[1] - 1] - i[2])
print(min_)
