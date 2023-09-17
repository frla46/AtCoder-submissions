m = int(input())
s = [input() for _ in range(3)]
ret = float('inf')
for i in range(m * 3):
    for j in range(m * 3):
        for k in range(m * 3):
            if i != j and i != k and j != k and s[0][i % m] == s[1][j % m] == s[2][k % m]:
                if ret > max(i, j, k):
                    ret = max(i, j, k)
print(ret if not ret == float('inf') else -1)
