a = int(input())
b = int(input())
c = int(input())
x = int(input())
cnt = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if i * 500 + j * 100 + k * 50 == x:
                cnt += 1
print(cnt)
