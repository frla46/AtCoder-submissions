s = input()
min_ = float('inf')
for i in range(len(s) - 2):
    min_ = min(abs(753 - int(s[i:i+3])), min_)
print(min_)
