n = int(input())
b = [int(i) for i in input().split()]
sum = b[0] + b[-1]
for i in range(n - 2):
    sum += min(b[i], b[i + 1])
print(sum)
