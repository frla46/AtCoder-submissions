n = int(input())
l = [int(i) for i in input().split()]
l.sort()
a_sum, b_sum = 0, 0
for n, i in enumerate(l):
    if n % 2 == 0:
        a_sum += i
    else:
        b_sum += i
print('{}'.format(abs(a_sum - b_sum)))
