s = input()
max = 0
l = len(s)
for i in range(l + 1):
    for j in range(i + 1, l + 1):
        t = s[i:j]
        # print(i, j, t)
        if t == t[::-1]:
            if j - i > max:
                max = j - i
print(max)
