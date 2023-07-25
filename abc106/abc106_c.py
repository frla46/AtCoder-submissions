s = input()
k = int(input())
c = 0
t = ''
for i in s:
    if i == '1':
        c += 1
    else:
        t = i
        break
print(t if k > c else '1')
