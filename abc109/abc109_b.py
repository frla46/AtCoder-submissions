n = int(input())
w = [input() for _ in range(n)]
if len(w) != len(set(w)):
    print('No')
    exit()
for i in range(1, n):
    if w[i - 1][-1] != w[i][0]:
        print('No')
        exit()
print('Yes')
