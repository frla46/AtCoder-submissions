n = int(input())
a = [int(i) for i in input().split()]
print('Yes' if len(set(a)) == 1 else 'No')
