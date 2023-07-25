n, m = [int(i) for i in input().split()]
ac = set()
wa = []
c_wa = 0
for _ in range(m):
    p, s = input().split()
    p = int(p)
    if int(p) in ac:
        continue
    else:
        if s == 'AC':
            ac.add(p)
            c_wa += wa.count(p)
        else:
            wa.append(p)
print('{} {}'.format(len(ac), c_wa))
