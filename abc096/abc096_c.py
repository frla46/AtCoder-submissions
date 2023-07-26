h, w = [int(i) for i in input().split()]
s = [input() for _ in range(h)]
tup = ((-1, 0), (1, 0), (0, -1), (0, 1))
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            flg = False
            for t in tup:
                if 0 <= i + t[0] <= h - 1 and 0 <= j + t[1] <= w - 1:
                    if s[i + t[0]][j + t[1]] == '#':
                        flg = True
            if not flg:
                print('No')
                exit()
print('Yes')


