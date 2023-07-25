n, a, b = [int(i) for i in input().split()]
sm = 0
for i in range(1, int(n) + 1):
    if a <= sum([int(c) for c in str(i)]) <= b:
        sm += i
print(sm)
