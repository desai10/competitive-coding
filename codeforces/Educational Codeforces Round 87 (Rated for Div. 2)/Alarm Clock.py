t = int(input())

while t > 0:

    a, b, c, d = [int(x) for x in input().split()]

    rem = a - b

    ct = min(a, b)

    if rem > 0:
        if d >= c:
            ct = -1
        else:
            dd = rem // (c - d)
            ct += dd * c
            ct += (0 if (rem % (c - d) == 0) else c)
    else:
        ct = b

    print(ct)

    t -= 1
