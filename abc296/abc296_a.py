n = int(input())
s = input()
for i, j in zip(s, s[1:]):
    if i == j:
        print('No')
        break
else:
    print('Yes')
