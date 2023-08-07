n, m = [int(i) for i in input().split()]
if n * 2 <= m:
    cnt = n + (m - 2 * n) // 4
else:
    cnt = m // 2
print(cnt)
