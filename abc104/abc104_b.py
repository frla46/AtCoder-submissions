s = input()
if s[0] == 'A' and s[2:-1].count('C') == 1 \
    and sum(1 for i in s if i.isupper()) == 2:
    print('AC')
else:
    print('WA')
