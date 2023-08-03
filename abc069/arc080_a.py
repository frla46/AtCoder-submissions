n = int(input())
a = [int(i) for i in input().split()]
four = sum([1 for i in a if i % 4 == 0])
two = sum([1 for i in a if i % 2 == 0]) - four
if four + two // 2 >= n // 2:
    print('Yes')
else:
    print('No')

