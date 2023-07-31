n = int(input())
a = [int(i) for i in input().split()]
cnt, is_inc = 0, 0
for i in range(1, n):
    d = a[i] - a[i - 1]
    if is_inc == 0:
        if d > 0:
            is_inc = 1
        elif d < 0:
            is_inc = -1
    elif is_inc == 1:
        if d < 0:
            is_inc = 0
            cnt += 1
    elif is_inc == -1:
        if d > 0:
            is_inc = 0
            cnt += 1
print(cnt + 1)


