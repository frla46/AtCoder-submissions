al = sum([list(map(int, input().split())) for _ in range(3)], [])
n = int(input())
bl = [int(input()) for _ in range(n)]
resl = [0] * 9
flg = 0
for n, i in enumerate(al):
    if i in bl:
        resl[n] = 1
if resl[0] == 1 and resl[1] == 1 and resl[2] == 1:
    flg = 1
elif resl[3] == 1 and resl[4] == 1 and resl[5] == 1:
    flg = 1
elif resl[6] == 1 and resl[7] == 1 and resl[8] == 1:
    flg = 1
elif resl[0] == 1 and resl[3] == 1 and resl[6] == 1:
    flg = 1
elif resl[1] == 1 and resl[4] == 1 and resl[7] == 1:
    flg = 1
elif resl[2] == 1 and resl[5] == 1 and resl[8] == 1:
    flg = 1
elif resl[0] == 1 and resl[4] == 1 and resl[8] == 1:
    flg = 1
elif resl[2] == 1 and resl[4] == 1 and resl[6] == 1:
    flg = 1
print('Yes' if flg == 1 else 'No')
