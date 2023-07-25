n, m, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
print(min(len([i for i in a if i < x]), len([i for i in a if i > x])))
