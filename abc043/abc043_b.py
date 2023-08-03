

s = input()
ret = ''
for c in s:
    if c == '0' or c == '1':
        ret += c
    elif c == 'B':
        ret = ret[:-1]
print(ret)
