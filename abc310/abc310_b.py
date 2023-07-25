n, m = [int(i) for i in input().split()]
li = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    for j in  range(n):
        if li[i][0] < li[j][0] and all([k in li[i][2:] for k in li[j][2:]]):
            print('Yes')
            exit()
        elif li[i][0] <= li[j][0] and \
            all([k in li[i][2:] for k in li[j][2:]]) and \
            len(li[i][2:]) > len(li[j][2:]):
            print('Yes')
            exit()
print('No')
