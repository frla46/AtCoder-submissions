n = int(input())
w = input().split()
l = ['and', 'not', 'that', 'the', 'you']
if any([i in l for i in w]):
    print('Yes')
else:
    print('No')
