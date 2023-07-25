n, m = [int(i) for i in input().split()]
li = [[int(i) for i in input().split()] for _ in range(m)]
li = sum(li, [])
for i in range(n):
    print(li.count(i + 1))
