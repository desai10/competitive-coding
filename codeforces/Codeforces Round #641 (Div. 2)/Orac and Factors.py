t = int(input())

while t > 0:

    n, k = [int(x) for x in input().split()]

    kk = -1

    for i in range(2, n + 1):
        if n % i == 0:
            kk = i
            break

    print(n + kk + (2 * (k - 1)))

    t -= 1
