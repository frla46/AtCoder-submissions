n = int(input())
d, x = [int(i) for i in input().split()]
ls = [int(input()) for _ in range(n)]
print(sum([(d - 1) // i + 1 for i in ls]) + x)
