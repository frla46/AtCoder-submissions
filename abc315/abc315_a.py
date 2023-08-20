s = [c for c in input()]
t = ['a', 'i', 'u', 'e', 'o']
s = [c for c in s if c not in t]
print(''.join(s))
