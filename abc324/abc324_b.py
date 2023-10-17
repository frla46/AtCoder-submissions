n = int(input())
for i in [2, 3]:
    while True:
        if n % i == 0:
            n /= i
        else:
            break
if n == 1:
    print('Yes')
else:
    print('No')
