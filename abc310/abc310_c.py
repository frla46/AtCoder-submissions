n = int(input())
s = set([input() for _ in range(n)])
memo = set()
for i in s:
    memo.add(min(i, i[::-1]))
print(len(memo))
