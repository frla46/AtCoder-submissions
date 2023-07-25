li = [int(i) for i in input().split()]
li.sort()
if sum([1 for i in li if i % 2 == 0]) == 0:
    print(li[0] *li[1])
else:
    print(0)
