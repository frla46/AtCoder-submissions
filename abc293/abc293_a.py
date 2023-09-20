s = input()
for a, b in zip(s[::2], s[1::2]):
    print(b, a, sep='', end='')
