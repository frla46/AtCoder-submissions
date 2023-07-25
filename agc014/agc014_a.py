a, b, c = [int(i) for i in input().split()]
cnt = 0
while True:
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        if a == b == c:
            cnt = -1
            break
        ta = a // 2
        tb = b // 2
        tc = c // 2
        a = tb + tc
        b = ta + tc
        c = ta + tb
        # print('{} {} {}'.format(a, b, c))
        cnt += 1
    else:
        break
print(cnt)
