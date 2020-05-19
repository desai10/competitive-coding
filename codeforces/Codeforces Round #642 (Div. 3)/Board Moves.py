t = int(input())

while t > 0 :

    n = int(input())

    ct = 0
    aa = 1

    for i in range(3, n + 1, 2):
        ct += ((i * 2 + ((i - 2) * 2)) * aa)
        aa += 1

    print(ct)

    t -= 1
