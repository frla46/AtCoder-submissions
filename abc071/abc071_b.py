s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for c in alphabet:
    if c not in s:
        print(c)
        exit()
print('None')
