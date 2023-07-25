n = int(input())
c = 0
while True:
    c += 1
    if 2 ** c > n:
        break
print(2 ** (c-1))
