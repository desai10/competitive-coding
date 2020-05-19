t = int(input())

while t > 0:

    a, k = [int(x) for x in input().split()]

    newa = a
    a = -1
    i = 1

    while newa != a and i < k:
        a = newa
        newa += (int(min(str(newa))) * int(max(str(newa))))
        i += 1

    print(newa)

    t -= 1
