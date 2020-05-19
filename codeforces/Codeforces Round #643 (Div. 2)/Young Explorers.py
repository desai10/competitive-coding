t = int(input())

while t > 0:

    n = int(input())
    e = [int(x) for x in input().split()]
    e.sort()

    cts = {}

    ct = 0
    req = e[0]
    cur = 0

    for x in e:
        if 

    rem = 0
    for key in cts:
        ct += (rem + cts[key]) // key
        rem = (rem + cts[key]) % key

    print(ct)

    t -= 1
