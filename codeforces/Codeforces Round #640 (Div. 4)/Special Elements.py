t = int(input())

while t > 0:

    n = int(input())

    arr =  [int(x) for x in input().split()]

    pres = [0 for _ in range(n + 1)]

    for (i, x) in enumerate(arr, 1):
        pres[i] = pres[i - 1] + x

    ct = 0
    if len(arr) > 1:
        for (i, x) in enumerate(arr):
            isPos = False
            l = 0
            r = 1
            cur = arr[0] + arr[1]
            while r < n and not isPos:
                if cur == x:
                    isPos = True
                    continue
                if cur > x:
                    cur -= arr[l]
                    l += 1
                else:
                    r += 1
                    if r < n:
                        cur += arr[r]

                if l == r:
                    r = l + 1
                    if r < n:
                        cur = arr[l] + arr[r]

            if isPos:
                ct += 1
                # print(i, x)

    print(ct)

    t -= 1
