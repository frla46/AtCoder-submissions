n, a, b = [int(i) for i in input().split()]
l = [s for s in input()]
total = 0
kaigai = 0
for i in l:
    if i == 'a' and total < a + b:
        print('Yes')
        total += 1
    elif i == 'b' and total < a + b and kaigai < b:
        print('Yes')
        total += 1
        kaigai += 1
    else:
        print('No')
