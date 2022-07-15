t = int(input())

while t > 0:

    n = int(input())

    l = 1
    r = n

    while l <= r:
        m = (l + r) // 2
        print ("?", l, m)
        nn = m - l + 1
        arr = [int(x) for x in input().split()]
        
        ct = 0
        for x in arr:
            if x >= l and x <= m:
                ct += 1

        if l == r:
            print("!", l)
            break

        if ct % 2 != 0:
            r = m
            if l == m:
                print("!", l)
                break
        else:
            l = m + 1

    t -= 1
