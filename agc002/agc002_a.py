a, b = [int(i) for i in input().split()]
if a > 0:
    ret = 'Positive'
elif a <= 0 <= b:
    ret = 'Zero'
else:
    if abs(a - b) % 2 == 0:
        ret = 'Negative'
    else:
        ret = 'Positive'
print(ret)
