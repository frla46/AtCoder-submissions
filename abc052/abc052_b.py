n = int(input())
s = input()
max = 0
cnt = 0
for c in s:
    if c == 'I':
        cnt += 1
    elif c == 'D':
        cnt -= 1
    if max < cnt:
        max = cnt
print(max)
