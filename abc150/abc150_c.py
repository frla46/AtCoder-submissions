from itertools import permutations
n = int(input())
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
li = [list(c) for c in permutations(range(1, n + 1), n)]
print(abs(li.index(p) - li.index(q)))
