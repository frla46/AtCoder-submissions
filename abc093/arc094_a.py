li = [int(i) for i in input().split()]
diff = sum([max(li) - i for i in li])
print(diff // 2 if diff % 2 == 0 else diff // 2 + 2)
