w, h, x, y = [int(i) for i in input().split()]
print(w * h / 2, 1 if w / 2 == x and h / 2 == y else 0)
