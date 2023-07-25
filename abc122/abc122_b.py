s = input()
ret = 0
l = 'ACGT'
for i in range(len(s)):
    c = 0
    for j in range(i, len(s)):
        if s[j] in l:
            c += 1
            ret = max(ret, c)
        else:
            break
print(ret)
