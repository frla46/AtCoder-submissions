n, m = [int(i) for i in input().split()]
li = [list(map(int, input().split())) for _ in range(m)]
left = [i[0] for i in li]
right = [i[1] for i in li]
print(max(0, min(right) - max(left) + 1))
