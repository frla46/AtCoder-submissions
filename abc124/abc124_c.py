s = input()
t = ''.join(['0' if i % 2 == 0 else '1' for i in range(len(s))])
cnt = 0
for i, j in zip(s, t):
    if i == j:
        cnt += 1
print(min(cnt, len(s) - cnt))
