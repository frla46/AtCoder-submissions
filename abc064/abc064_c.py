n = int(input())
a = [int(i) for i in input().split()]
li = []
for i in a:
    group = i // 400
    if 0 <= group <= 7:
        li.append(group)
colors = len(set(li))
cnt = sum([1 for i in a if i >= 3200])
print(colors if colors != 0 else 1, colors + cnt)
