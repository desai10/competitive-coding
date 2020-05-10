t = int(input())

while t > 0:

    n, k = [int(x) for x in input().split()]

    tt = (k // (n - 1))
    ans = (tt * n) + (k % (n - 1))
    if k % (n - 1) == 0:
        ans -= 1
    print(ans)

    t -= 1
