t = int(input())

while t > 0:

    n = int(input())
    a = [int(x) for x in input().split()]

    al = 0
    bo = 0
    ct = 0

    mv = 1

    pre = a[0]
    al += a[0]
    ct += 1
    a.pop(0)

    while len(a) > 0:
        cur = 0
        if mv == 1:
            while cur <= pre:
                poped = a.pop()
                cur +=  poped
                if len(a) == 0:
                    break

            bo += cur

        else:
            while cur <= pre:
                poped = a.pop(0)
                cur += poped
                if len(a) == 0:
                    break

            al += cur

        mv = 1 - mv
        pre = cur
        ct += 1

        # print(ct, pre, al, bo, a)

    print(ct, al, bo)



    t -= 1
