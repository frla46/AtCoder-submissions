
h, w = [int(i) for i in input().split()]
s = [input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        # print(f'i:{i}, j:{j}')
        # print(s[i][j])
        if s[i][j] == '.':
            cnt = 0
            for u in range(-1, 2):
                for v in range(-1, 2):
                    # print(f'u:{u}, v:{v}')
                    if 0 <= i + u < h and 0<= j + v < w:
                        # print(f'u:{u}, v:{v}')
                        if s[i + u][j + v] == '#':
                            cnt += 1
            print(cnt, end='')
        else:
            print('#', end='')
    print()
