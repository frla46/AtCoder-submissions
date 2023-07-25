n, p, q = [int(i) for i in input().split()]
d =  [int(i) for i in input().split()]
print(min(p, q + min(d)))
