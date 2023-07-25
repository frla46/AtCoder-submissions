a, b, k = [int(i) for i in input().split()]
s = set()
for i in range(k):
    if a <= b - i:
        s.add(b - i)
    if a + i <= b:
        s.add(a + i)
s = sorted(list(s))
for i in s:
    print(i)
