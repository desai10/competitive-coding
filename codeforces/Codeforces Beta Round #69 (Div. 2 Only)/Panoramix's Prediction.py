def isPrime(n):
    ct = 0
    for i in range(1, n):
        if n % i == 0:
            ct += 1

    if ct > 1:
        return False
    return True

def doit():

    n, m = list(map(lambda x: int(x), input().split()))

    for i in range(n + 1, m):
        if isPrime(i):
            print('NO')
            return

    if isPrime(m):
        print('YES')
    else:
        print('NO')

doit()