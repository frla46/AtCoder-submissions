n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
max = 0
for i in set(s):
    score = s.count(i) - t.count(i)
    if max < score:
        max = score
print(max)
