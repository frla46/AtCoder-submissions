x = int(input())
i = x // 100
if x % 100 <= 5 * i:
    print(1)
else:
    print(0)
