n, k, q = [int(i) for i in input().split()]
a = [int(input()) for _ in range(q)]
li = [0] * n
for i in a:
    li[i - 1] += 1
for i in range(n):
    ret = 'Yes' if li[i] > q - k else 'No'
    print(ret)
