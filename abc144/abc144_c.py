import math
n = int(input())
for i in range(math.floor(math.sqrt(n)), 0, -1):
    if n % i == 0:
        print(i + n // i - 2)
        exit()
