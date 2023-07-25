n = int(input())
max = sum([int(c) for c in str(n)])
for i in range(1, len(str(n))):
    s = str(n - n % 10 ** i - 1)
    t = sum([int(c) for c in s])
    if max < t:
        max = t
print(max)
