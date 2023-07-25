n = int(input())
a = [int(i) for i in input().split()]
print(sum([format(i, 'b')[::-1].find('1') for i in a]))
