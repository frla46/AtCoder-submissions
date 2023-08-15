w, h, n = [int(i) for i in input().split()]
l = [[int(i) for i in input().split()] for _ in range(n)]
xl = max([0] + [i[0] for i in l if i[2] == 1])
xr = min([w] + [i[0] for i in l if i[2] == 2])
yl = max([0] + [i[1] for i in l if i[2] == 3])
yr = min([h] + [i[1] for i in l if i[2] == 4])
print(max(0, (xr - xl)) * max(0, (yr - yl)))
