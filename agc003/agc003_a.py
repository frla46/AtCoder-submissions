s = set(input())
if 'N' in s and 'S' in s:
    s.remove('N')
    s.remove('S')
if 'W' in s and 'E' in s:
    s.remove('W')
    s.remove('E')
if len(s) == 0:
    print("Yes")
else:
    print("No")
