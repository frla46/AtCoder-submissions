n, k = [int(i) for i in input().split()]
h = [int(input()) for _ in range(n)]
h.sort()
min = float('inf')
for i in range(n - k + 1):
    t = h[i + k - 1] - h[i]
    if min > t:
        min = t
print(min)
