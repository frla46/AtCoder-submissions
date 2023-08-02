

n = int(input())
s = input()
t = input()
for i in range(n):
    if all([a == b for a, b in zip(s[i:], t)]):
        print(n + i)
        exit()
else:
    print(n * 2)
