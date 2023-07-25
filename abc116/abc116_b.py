s = int(input())
l = []
c = 0
while s not in l:
    l.append(s)
    s = s / 2 if s % 2 == 0 else 3 * s + 1
    c += 1
print(c + 1)
