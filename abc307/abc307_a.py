n = int(input())
a = [int(i) for i in input().split()]
s = 0
c = 0
for i in a:
    c += 1
    s += i
    if c == 7:
        print(s, end=' ')
        s = 0
        c = 0
