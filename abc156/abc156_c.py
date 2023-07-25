n = int(input())
l = [int(i) for i in input().split()]
min_ = float('inf')
for i in range(1, 101):
    sum_ = sum([(j - i) ** 2 for j in l])
    min_ = min(sum_, min_)
print(min_)
