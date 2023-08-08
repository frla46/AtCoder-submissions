s = input()
f = s.count('a'), s.count('b'), s.count('c')
if max(f) - min(f) <= 1:
    print('YES')
else:
    print('NO')
