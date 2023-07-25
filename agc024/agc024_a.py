a, b, c, k = [int(i) for i in input().split()]
ret = pow(-1, k) * (a - b)
if abs(ret) > 10 ** 18:
    print('Unfair')
else:
    print(ret)
