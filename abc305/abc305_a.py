n = int(input())
min = float('inf')
p = 0
for i in range(0, 101, 5):
    l = abs(n - i)
    if min > l:
        min = l
        p = i
print(p)
