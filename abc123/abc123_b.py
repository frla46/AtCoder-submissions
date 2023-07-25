li = [int(input()) for _ in range(5)]
sum = 0
min = 10
for i in li:
    if i % 10 == 0:
        sum += i
    else:
        sum += i // 10 * 10 + 10
        if i % 10 < min:
            min = i % 10
print(sum - 10 + min)
