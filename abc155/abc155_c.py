import collections
n = int(input())
s = [input() for _ in range(n)]
c = collections.Counter(s).most_common()
ret = []
for i in c:
    if not c[0][1] == i[1]:
        break
    ret.append(i[0])
for i in sorted(ret):
    print(i)
