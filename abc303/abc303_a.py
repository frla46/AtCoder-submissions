n = int(input())
s = input()
t = input()
for i, j in zip(s, t):
    if i == '0':
        i = 'o'
    if j == '0':
        j = 'o'
    if i == '1':
        i = 'l'
    if j == '1':
        j = 'l'
    if i != j:
        print('No')
        exit()
print('Yes')
