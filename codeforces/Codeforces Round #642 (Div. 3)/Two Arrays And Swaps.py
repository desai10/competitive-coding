t = int(input())

while t > 0:

    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    a.sort()

    tot = 0

    for i in range(0, n):
        the = 0
        for j in range(1, n):
            if b[j] > a[i] and b[the] < b[j]:
                the = j

        if b[the] > a[i] and tot < k:
            aaa = a[i]
            a[i] = b[the]
            b[the] = aaa
            tot += 1

        if tot >= k:
            break

        # print(i, the, a, b)

    ct = 0
    for x in a:
        ct += x

    print(ct)


    t -= 1
