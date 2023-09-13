n = int(input())
s = input()
p = s.find('*')
if '|' in s[:p] and '|' in s[p:]:
    print('in')
else:
    print('out')
