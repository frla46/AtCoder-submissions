n = input()
for i, j in zip(n, n[1:]):
    if not int(i) > int(j):
        print('No')
        exit()
print('Yes')
