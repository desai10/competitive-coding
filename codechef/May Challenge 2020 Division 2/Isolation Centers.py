t = int(input())

while t > 0:

    n, q = [int(x) for x in input().split()]
    s = input()

    ma = {}

    for c in s:
        if c not in ma:
            ma[c] = 0

        ma[c] += 1

    while q > 0:

        c = int(input())

        ct = 0

        for key in ma:
            ct += max(0, ma[key] - c)

        print (ct)

        q -= 1

    t -= 1
