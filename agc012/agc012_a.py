n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
print(sum(a[1:n * 2 + 1:2]))
