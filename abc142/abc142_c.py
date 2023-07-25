n = int(input())
a = [int(i) for i in input().split()]
t = sorted([[n, i] for n, i in enumerate(a)], key = lambda x : x[1])
print(' '.join([str(i[0] + 1) for i in t]))
