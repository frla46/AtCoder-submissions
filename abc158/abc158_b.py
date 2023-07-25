n, a, b = [int(i) for i in input().split()]
t = n % (a + b) if n % (a + b) < a else a
print(n // (a + b) * a + t)
