a, b, c, d = input()
o = '+-'
for i in range(8):
    s = a + o[i & 1] + b + o[(i & 2) >> 1] + c + o[(i & 4) >> 2] + d
    if eval(s) == 7:
        print(f'{s}=7')
        exit()
