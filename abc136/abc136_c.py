n = int(input())
h = [int(i) for i in input().split()]
for i in range(1, n):
    if h[i - 1] <= h[i] - 1:
        h[i] -= 1
    elif h[i - 1] == h[i]:
        pass
    else:
        print('No')
        exit()
print('Yes')
