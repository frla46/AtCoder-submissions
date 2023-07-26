import collections
n = int(input())
a = [int(i) for i in input().split()]
li = []
for i in a:
    li += [i - 1, i, i + 1]
print(collections.Counter(li).most_common()[0][1])

