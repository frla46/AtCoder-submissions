
s = input()
ret = [0] * (len(s) + 1)
for i in range(len(s)):
    if s[i] == '<':
        ret[i + 1] = max(ret[i] + 1, ret[i + 1])
for i in range(len(s) - 1, -1, -1):
    if s[i] == '>':
        ret[i] = max(ret[i], ret[i + 1] + 1)
print(sum(ret))
