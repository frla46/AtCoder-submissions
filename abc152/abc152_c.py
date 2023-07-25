n = int(input())
li = [int(i) for i in input().split()]
min = float('inf')
cnt = 0
for i in li:
    if min > i:
        min = i
        cnt += 1
print(cnt)
