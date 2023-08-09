n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
x, y= 0, 0
i = 0
while i < n - 1:
    if a[i] == a[i + 1]:
        if x == 0:
            x = a[i]
        else:
            y = a[i]
            break
        i += 1
    i += 1
print(x * y)
