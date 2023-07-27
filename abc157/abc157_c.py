n, m = [int(i) for i in input().split()]
li = [[int(i) for i in input().split()] for _ in range(m)]
for i in range(10 ** n):
    if len(str(i)) != n:
        continue
    if all([str(i)[a - 1] == str(b) for a, b in li]):
        print(i)
        exit()
print(-1)


