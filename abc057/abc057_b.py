n, m = [int(i) for i in input().split()]
li_a = [[int(i) for i in input().split()] for _ in range(n)]
li_b = [[int(i) for i in input().split()] for _ in range(m)]
for i in li_a:
    min = float('inf')
    num = 0
    for x, j in enumerate(li_b):
        len = abs(j[0] - i[0]) + abs(j[1] - i[1])
        if min > len:
            min = len
            num = x + 1
    print(num)



