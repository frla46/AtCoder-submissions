n, m = [int(i) for i in input().split()]
s = [input() for _ in range(n)]
hash = ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8))
dot = ((0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (3, 0), (5, 5), (5, 6), (5, 7), (5, 8), (6, 5), (7, 5), (8, 5))
for i in range(n - 8):
    for j in range(m - 8):
        if all([s[i + u][j + v] == '#' for u, v in hash]) and all([s[i + u][j + v] == '.' for u, v in dot]):
            print(i + 1, j + 1)


