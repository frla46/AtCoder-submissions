n = int(input())
t, a = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
# print(h.index(int(min([abs(t - i * 0.006) for i in h]))))
min = float('inf')
index = 0
for i, j in enumerate(h):
    tmp = abs(a - (t - j * 0.006))
    if tmp < min:
        min = tmp
        index = i
print(index + 1)
