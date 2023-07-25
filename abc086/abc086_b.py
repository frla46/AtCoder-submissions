a, b = input().split()
tmp = int(a + b)
flg = 0
for i in range(1001):
    if tmp == i ** 2:
        flg = 1
print('Yes' if flg == 1 else 'No')
