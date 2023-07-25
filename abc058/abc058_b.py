import itertools
o = input()
e = input()
for i, j in itertools.zip_longest(o, e, fillvalue=''):
    print(f'{i}{j}', end='')
