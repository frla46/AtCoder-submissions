s = input()
while True:
    s = s[:-2]
    l = len(s) // 2
    if s[:l] == s[l:]:
        print(len(s))
        exit()

