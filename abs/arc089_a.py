n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    if i == 0:
        if l[i][0] < l[i][1] + l[i][2] or l[i][0] % 2 != (l[i][1] + l[i][2]) % 2:
            print('No')
            exit()
    else:
        if abs(l[i][0] - l[i-1][0]) < abs(l[i][1] - l[i-1][1]) + abs(l[i][2] - l[i-1][2]) or l[i][0] % 2 != (l[i][1] + l[i][2]) % 2:
            print('No')
            exit()
print('Yes')
