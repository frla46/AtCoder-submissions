n = int(input())
li = [int(input()) for _ in range(n)]
soli = sorted(li, reverse=True)
for i in range(n):
    if li[i] != soli[0]:
        print(soli[0])
    else:
        print(soli[1])
