n = int(input())
k = int(input())
x = [int(i) for i in input().split()]
print(sum([min(abs(i), abs(i - k)) * 2 for i in x]))
