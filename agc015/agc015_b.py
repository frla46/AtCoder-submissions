s = input()
cnt = len(s) * (len(s) - 1)
for i in range(len(s)):
    if s[i] == 'U':
        cnt += i
    else:
        cnt += len(s) - i - 1
print(cnt)
