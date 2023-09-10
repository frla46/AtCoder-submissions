n = int(input())
for i in range(n + 1):
    for j in range(1, 10):
        if n % j == 0 and i % (n / j) == 0:
            c = j
            break
    else:
        c = '-'
    print(c, end='')
