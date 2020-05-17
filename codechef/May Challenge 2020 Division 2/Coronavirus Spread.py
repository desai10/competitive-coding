t = int(input())

while t > 0:

    n = int(input())
    arr = [int(x) for x in input().split()]

    mx = -1
    mi = 10

    for i in range(n):
        ti = i - 1
        pre = i
        ct = 1
        while ti >= 0:
            if abs(arr[ti] - arr[pre]) <= 2:
                ct += 1
                pre = ti
            else:
                break
            ti -=  1

        ti = i + 1
        pre = i

        while ti < n:

            if abs(arr[ti] - arr[pre]) <= 2:
                ct += 1
                pre = ti
            else:
                break
            ti += 1

        if ct > mx:
            mx = ct
        if ct < mi:
            mi = ct

    print(mi, mx)


    t -= 1