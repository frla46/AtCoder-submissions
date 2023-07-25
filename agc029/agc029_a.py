s = input()
cnt = 0
b_cnt = 0
for i in s:
    if i == 'B':
        b_cnt += 1
    if i == 'W':
        cnt += b_cnt
print(cnt)
