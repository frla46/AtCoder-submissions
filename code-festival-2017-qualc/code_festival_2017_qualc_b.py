n = int(input())
a = [int(i) for i in input().split()]
x = 1
for i in a:
    if i % 2 == 0:
        x *= 2
    else:
        x *= 1
print(3 ** n - x)
