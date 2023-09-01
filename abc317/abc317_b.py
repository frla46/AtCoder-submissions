n = int(input())
a = set([int(i) for i in input().split()])
for i in range(min(a), max(a) + 1):
    if not i in a:
        print(i)
        exit()
