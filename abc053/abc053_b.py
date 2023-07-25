s = input()
sr = s[::-1]
print(len(s) - sr.index('Z') - s.index('A'))
