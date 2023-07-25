import math
x = int(input())
max = 0
for i in range(1, math.ceil(math.sqrt(x)) + 1):
    for j in range(1, math.ceil(math.sqrt(x)) + 1):
        if max < i ** j <= x:
            max = i ** j
print(max)
