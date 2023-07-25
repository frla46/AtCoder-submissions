n, k = [int(i) for i in input().split()]
min_ = float('inf')
while True:
    if n > k:
        n = n % k
    else:
        n = abs(n - k)
        if min_ > n:
            min_ = n
        else:
            break
print(min_)
