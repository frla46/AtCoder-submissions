s = input()
for i in range(26):
    c = s.count(chr(ord('a') + i))
    if c % 2 != 0:
        print('No')
        exit()
print('Yes')
