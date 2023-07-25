a, b = [int(i) for i in input().split()]
s = input()
num = '0123456789'
if all([c in num for c in s[0:a]]) \
    and s[a] == '-' \
    and all([c in num for c in s[-b:]]):
    print('Yes')
else:
    print('No')
