s = list(input())
min = float('inf')
for a in range(ord('a'),  ord('a') + 26):
    cnt = 0
    a = chr(a)
    t = list(s)
    while len(set(t)) != 1:
        cnt += 1
        for i in range(len(t) - 1):
            if t[i + 1] == a:
                t[i] = a
        del t[-1]
    if min > cnt:
        min = cnt
print(min)