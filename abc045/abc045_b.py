a = input() + '0'
b = input() + '0'
c = input() + '0'
t = 'a'
ca, cb, cc = 0, 0, 0
while True:
    if t == 'a':
        if a[ca] == '0':
            print('A')
            exit()
        t = a[ca]
        ca += 1
    if t == 'b':
        if b[cb] == '0':
            print('B')
            exit()
        t = b[cb]
        cb += 1
    if t == 'c':
        if c[cc] == '0':
            print('C')
            exit()
        t = c[cc]
        cc += 1

