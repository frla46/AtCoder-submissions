import math
n = int(input())
for i in range(50000):
    if n == math.floor(i * 1.08):
        print(i)
        exit()
print(':(')
