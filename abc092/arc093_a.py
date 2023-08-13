n = int(input())
a = [0] + [int(i) for i in input().split()] + [0]
sum = 0
for i in range(1, n + 2):
    sum += abs(a[i] - a[i - 1])
for i in range(1, n + 1):
    if a[i - 1] <= a[i] <= a[i + 1] or a[i + 1] <= a[i] <= a[i - 1]:
        print(sum)
    else:
        l = min(abs(a[i] - a[i - 1]), abs(a[i] - a[i + 1])) * 2
        print(sum - l)
