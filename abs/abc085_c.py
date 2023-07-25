n, y = [int(i) for i in input().split()]
for i in range(n + 1):
    for j in range(n - i + 1):
        if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
            print('{} {} {}'.format(i, j, n - i - j))
            exit()
print('-1 -1 -1')
