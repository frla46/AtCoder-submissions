n = int(input())
s = input()
ca = s.count('A')
ct = s.count('T')
if ca > ct:
    print('A')
elif ca < ct:
    print('T')
else:
    if s[-1] == 'A':
        print('T')
    else:
        print('A')
