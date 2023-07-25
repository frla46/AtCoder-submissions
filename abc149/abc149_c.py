import math
x = int(input())
def isPrime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True
while True:
    if isPrime(x):
        print(x)
        exit()
    else:
        x += 1
