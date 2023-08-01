

s = sorted(input())
t = sorted(input(), reverse=True)
for a, b in zip(s, t):
    if a < b:
        print('Yes')
        exit()
    if a > b:
        print('No')
        exit()
if len(s) < len(t):
    print('Yes')
else:
    print('No')
